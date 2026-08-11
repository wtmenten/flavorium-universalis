import argparse
import os
import re
import sys
import json
import html
import hashlib
import time
import urllib.request
import urllib.parse
import urllib.error
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv
import tomllib

# DeepL is optional: only required when a "deepl" translator is actually selected.
try:
	import deepl
except ImportError:
	deepl = None

# ==========================================
# CONFIGURATION
# ==========================================

load_dotenv()
AUTH_KEY = os.getenv("DEEPL_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-3-flash-preview"
GEMINI_API_BASE = "https://generativelanguage.googleapis.com/v1beta/models"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
SUBMODS_DIR = os.path.join(ROOT_DIR, "submods")

# Localization lives under several content roots; each holds <root>/localization/<language>/.
LOC_CONTENT_ROOTS = ("in_game", "main_menu", "loading_screen")
CONFIG_PATH = os.path.join(SCRIPT_DIR, "config.toml")
METADATA_PATH = os.path.join(ROOT_DIR, ".metadata", "metadata.json")
WORKSHOP_DESCRIPTION_PATH = os.path.join(ROOT_DIR, "WORKSHOP_DESCRIPTION_steam.bbcode")
WORKSHOP_TRANSLATIONS_DIR = os.path.join(ROOT_DIR, "assets", "workshop", "translations")
WORKSHOP_TRANSLATION_FILENAME = "workshop_{lang}.txt"
CHANGE_NOTES_PATH = os.path.join(ROOT_DIR, "assets", "workshop", "change-notes.bbcode")
# Per-version change notes live in docs/change_notes/<version>.bbcode and take precedence
# over the shared multi-version archive above (matching upload.py's resolution order).
CHANGE_NOTES_DIR = os.path.join(ROOT_DIR, "docs", "change_notes")
CHANGE_NOTES_TRANSLATION_FILENAME = "change-notes_{lang}.txt"
WORKSHOP_TRANSLATION_TEMPLATE_PATH = os.path.join(WORKSHOP_TRANSLATIONS_DIR, "translation_template.txt")
WORKSHOP_TITLE_MARKER = "===WORKSHOP_TITLE==="
WORKSHOP_DESCRIPTION_MARKER = "===WORKSHOP_DESCRIPTION==="
WORKSHOP_NO_TRANSLATE_BELOW = "--NO-TRANSLATE-BELOW--"
WORKSHOP_ITEM_ID_TOKEN = "$item-id$"
# Matches both the markdown form (``# v1.0:``) and the BBCode form (``[b]v1.0:[/b]``)
# used by assets/workshop/change-notes.bbcode.
CHANGE_NOTES_VERSION_RE = re.compile(
	r"^(?:#\s*|\[b\])(v(.+?)(:\s*|\s*))(?:\[/b\])?$"
)

LOCAL_TRANSLATOR = "local"
ALLOWED_WORKSHOP_DESCRIPTION_TRANSLATORS = {"deepl", "gemini-3-flash", LOCAL_TRANSLATOR}
ALLOWED_WORKSHOP_TITLE_TRANSLATORS = {"deepl", "gemini-3-flash", LOCAL_TRANSLATOR}
ALLOWED_LOCALIZATION_TRANSLATORS = {"deepl", "gemini-3-flash", LOCAL_TRANSLATOR}

LANGUAGE_CONFIG = {
	"english": {"deepl": "EN", "loc_id": "l_english"},
	"french": {"deepl": "FR", "loc_id": "l_french"},
	"german": {"deepl": "DE", "loc_id": "l_german"},
	"spanish": {"deepl": "ES", "loc_id": "l_spanish"},
	"polish": {"deepl": "PL", "loc_id": "l_polish"},
	"russian": {"deepl": "RU", "loc_id": "l_russian"},
	"simp_chinese": {"deepl": "ZH", "loc_id": "l_simp_chinese"},
	"turkish": {"deepl": "TR", "loc_id": "l_turkish"},
	"braz_por": {"deepl": "PT", "loc_id": "l_braz_por"},
	"japanese": {"deepl": "JA", "loc_id": "l_japanese"},
	"korean": {"deepl": "KO", "loc_id": "l_korean"}
}

TARGET_LANGUAGES = {
	"english": "EN",
	"polish": "PL",
	"russian": "RU",
	"simp_chinese": "ZH",
	"spanish": "ES",
	"turkish": "TR",
	"braz_por": "PT-BR",
	"french": "FR",
	"german": "DE",
	"japanese": "JA",
	"korean": "KO"
}

LANGUAGE_DISPLAY_NAMES = {
	"english": "English",
	"polish": "Polish",
	"russian": "Russian",
	"simp_chinese": "Simplified Chinese",
	"spanish": "Spanish",
	"turkish": "Turkish",
	"braz_por": "Portuguese (Brazil)",
	"french": "French",
	"german": "German",
	"japanese": "Japanese",
	"korean": "Korean"
}

# Cache of source key/value hashes to avoid re-translating unchanged lines.
HASHES_PATH = os.path.join(SCRIPT_DIR, "dependencies", ".translate_hashes.json")
HASH_FILE_VERSION = 1

KEY_VALUE_RE = re.compile(r'^(\s*)([^:#]+):\s*"(.*)"(.*)$')
HEADER_RE = re.compile(r'^\s*l_[^:]+:\s*$')
LOCK_RE = re.compile(r'#\s*LOCK\b')
XML_PLACEHOLDER_TAG = "locvar"

# Markup that must survive translation verbatim: escaped newlines, [scope.Function] and
# [Concept('x','y')] links, $VARIABLE$ tokens, @icon! sprites, #colour ... #! blocks and
# £icon£ sprites.
MARKUP_TOKEN_RE = re.compile(
	r'\\n|\[[^\]]*\]|\$[^$]*\$|@[A-Za-z0-9_]+!|£[A-Za-z0-9_]+£|#!|#[A-Za-z0-9_;]+'
)

def deepl_split_sentences_off():
	"""Lazily resolve DeepL's SplitSentences.OFF (deepl is an optional dependency)."""
	return deepl.api_data.SplitSentences.OFF

# Settings for the local OpenAI-compatible server, populated from config.toml in main().
LOCAL_SETTINGS = {
	"api_base": "http://127.0.0.1:9292/v1",
	"model": "",
	"api_key": "",
	"batch_size": 25,
	"concurrency": 3,
	"temperature": 0.2,
	"max_tokens": 8192,
	"disable_thinking": True,
	"timeout": 600,
}

# ==========================================
# LOGIC
# ==========================================

def _parse_positive_int(value, label):
	"""Parse a positive integer from config values."""
	try:
		parsed = int(value)
	except (TypeError, ValueError):
		print(f"Error: {label} must be an integer.")
		return None
	if parsed <= 0:
		print(f"Error: {label} must be a positive integer.")
		return None
	return parsed

def load_config(config_path):
	"""Load config.toml and validate required keys and values."""
	invalid = (None,) * 12

	if not os.path.exists(config_path):
		print(f"Error: Config file not found: {config_path}")
		return invalid

	try:
		with open(config_path, "rb") as f:
			data = tomllib.load(f)
	except Exception as e:
		print(f"Error reading config file: {e}")
		return invalid

	source_language = data.get("source_language")
	if not source_language:
		print(f"Error: source_language not set in {config_path}")
		return invalid

	source_language = str(source_language).strip().lower()

	if source_language not in LANGUAGE_CONFIG:
		valid = ", ".join(sorted(LANGUAGE_CONFIG.keys()))
		print(f"Error: Unsupported source_language '{source_language}'.")
		print(f"Supported values: {valid}")
		return invalid

	if "localization_translator" not in data:
		print(f"Error: localization_translator not set in {config_path}")
		return invalid
	localization_translator = data.get("localization_translator")
	if not isinstance(localization_translator, str):
		print("Error: localization_translator must be a string.")
		return invalid
	if localization_translator not in ALLOWED_LOCALIZATION_TRANSLATORS:
		valid = ", ".join(sorted(ALLOWED_LOCALIZATION_TRANSLATORS))
		print(f"Error: Unsupported localization_translator '{localization_translator}'.")
		print(f"Supported values: {valid}")
		return invalid

	if "gemini_localization_system_prompt" not in data:
		print(f"Error: gemini_localization_system_prompt not set in {config_path}")
		return invalid
	gemini_localization_system_prompt = data.get("gemini_localization_system_prompt")
	if not isinstance(gemini_localization_system_prompt, str) or not gemini_localization_system_prompt.strip():
		print("Error: gemini_localization_system_prompt must be a non-empty string.")
		return invalid

	if "translate_workshop" not in data:
		print(f"Error: translate_workshop not set in {config_path}")
		return invalid
	translate_workshop = data.get("translate_workshop")
	if not isinstance(translate_workshop, bool):
		print("Error: translate_workshop must be a boolean (true/false).")
		return invalid

	if "translate_submods_by_default" not in data:
		print(f"Error: translate_submods_by_default not set in {config_path}")
		return invalid
	translate_submods_by_default = data.get("translate_submods_by_default")
	if not isinstance(translate_submods_by_default, bool):
		print("Error: translate_submods_by_default must be a boolean (true/false).")
		return invalid

	translate_change_notes_by_default = data.get("translate_change_notes_by_default", False)
	if not isinstance(translate_change_notes_by_default, bool):
		print("Error: translate_change_notes_by_default must be a boolean (true/false).")
		return invalid

	if "workshop_description_translator" not in data:
		print(f"Error: workshop_description_translator not set in {config_path}")
		return invalid
	workshop_description_translator = data.get("workshop_description_translator")
	if not isinstance(workshop_description_translator, str):
		print("Error: workshop_description_translator must be a string.")
		return invalid
	if workshop_description_translator not in ALLOWED_WORKSHOP_DESCRIPTION_TRANSLATORS:
		valid = ", ".join(sorted(ALLOWED_WORKSHOP_DESCRIPTION_TRANSLATORS))
		print(f"Error: Unsupported workshop_description_translator '{workshop_description_translator}'.")
		print(f"Supported values: {valid}")
		return invalid

	if "workshop_title_translator" not in data:
		print(f"Error: workshop_title_translator not set in {config_path}")
		return invalid
	workshop_title_translator = data.get("workshop_title_translator")
	if not isinstance(workshop_title_translator, str):
		print("Error: workshop_title_translator must be a string.")
		return invalid
	if workshop_title_translator not in ALLOWED_WORKSHOP_TITLE_TRANSLATORS:
		valid = ", ".join(sorted(ALLOWED_WORKSHOP_TITLE_TRANSLATORS))
		print(f"Error: Unsupported workshop_title_translator '{workshop_title_translator}'.")
		print(f"Supported values: {valid}")
		return invalid

	if "gemini_description_system_prompt" not in data:
		print(f"Error: gemini_description_system_prompt not set in {config_path}")
		return invalid
	gemini_description_system_prompt = data.get("gemini_description_system_prompt")
	if not isinstance(gemini_description_system_prompt, str) or not gemini_description_system_prompt.strip():
		print("Error: gemini_description_system_prompt must be a non-empty string.")
		return invalid

	if "gemini_title_system_prompt" not in data:
		print(f"Error: gemini_title_system_prompt not set in {config_path}")
		return invalid
	gemini_title_system_prompt = data.get("gemini_title_system_prompt")
	if not isinstance(gemini_title_system_prompt, str) or not gemini_title_system_prompt.strip():
		print("Error: gemini_title_system_prompt must be a non-empty string.")
		return invalid

	gemini_additional_context = data.get("gemini_additional_context", "")
	if not isinstance(gemini_additional_context, str):
		print("Error: gemini_additional_context must be a string.")
		return invalid
	gemini_additional_context = gemini_additional_context.strip()

	# Local OpenAI-compatible server settings (llama.cpp / llama-swap / LM Studio / Ollama).
	selected = {localization_translator, workshop_description_translator, workshop_title_translator}
	if LOCAL_TRANSLATOR in selected:
		local_model = data.get("local_model")
		if not isinstance(local_model, str) or not local_model.strip():
			print(f"Error: local_model must be a non-empty string in {config_path} when using the 'local' translator.")
			return invalid
		LOCAL_SETTINGS["model"] = local_model.strip()

		api_base = data.get("local_api_base", LOCAL_SETTINGS["api_base"])
		if not isinstance(api_base, str) or not api_base.strip():
			print("Error: local_api_base must be a non-empty string.")
			return invalid
		LOCAL_SETTINGS["api_base"] = api_base.strip()

		api_key = data.get("local_api_key", "")
		if not isinstance(api_key, str):
			print("Error: local_api_key must be a string.")
			return invalid
		LOCAL_SETTINGS["api_key"] = api_key.strip()

		for key, label in (
			("local_batch_size", "batch_size"),
			("local_concurrency", "concurrency"),
			("local_max_tokens", "max_tokens"),
			("local_timeout_seconds", "timeout"),
		):
			if key in data:
				parsed = _parse_positive_int(data.get(key), key)
				if parsed is None:
					return invalid
				LOCAL_SETTINGS[label] = parsed

		if "local_temperature" in data:
			temperature = data.get("local_temperature")
			if not isinstance(temperature, (int, float)) or isinstance(temperature, bool) or temperature < 0:
				print("Error: local_temperature must be a non-negative number.")
				return invalid
			LOCAL_SETTINGS["temperature"] = float(temperature)

		if "local_disable_thinking" in data:
			disable_thinking = data.get("local_disable_thinking")
			if not isinstance(disable_thinking, bool):
				print("Error: local_disable_thinking must be a boolean (true/false).")
				return invalid
			LOCAL_SETTINGS["disable_thinking"] = disable_thinking

	# Defer validation — only required when workshop pages are actually translated.
	workshop_item_id = None
	raw_item_id = data.get("workshop_upload_item_id")
	if isinstance(raw_item_id, int) and raw_item_id > 0:
		workshop_item_id = raw_item_id

	return (
		source_language,
		translate_workshop,
		translate_submods_by_default,
		translate_change_notes_by_default,
		localization_translator,
		gemini_localization_system_prompt,
		workshop_description_translator,
		gemini_description_system_prompt,
		workshop_title_translator,
		gemini_title_system_prompt,
		gemini_additional_context,
		workshop_item_id
	)

def parse_args():
	"""Parse command line arguments."""
	parser = argparse.ArgumentParser(
		description="Translate localization and optional workshop text."
	)
	parser.add_argument(
		"-m", "--mod",
		action="store_true",
		help="Translate mod localization files. When set, config defaults are ignored."
	)
	parser.add_argument(
		"-wp", "--workshop-pages",
		action="store_true",
		help="Translate workshop title/description pages. When set, config defaults are ignored."
	)
	parser.add_argument(
		"-s", "--submods",
		action="store_true",
		help="Include all submods under submods/*. When set, config defaults are ignored."
	)
	parser.add_argument(
		"-cn", "--change-notes",
		action="store_true",
		help="Translate change notes. When set, config defaults are ignored."
	)
	parser.add_argument(
		"-l", "--languages",
		metavar="LANGS",
		help=(
			"Comma-separated target languages to translate (default: all supported). "
			"Valid: " + ", ".join(sorted(k for k in TARGET_LANGUAGES if k != "english"))
		)
	)
	return parser.parse_args()

def resolve_target_languages(languages_arg, source_language):
	"""Resolve the target language set, honouring an optional --languages filter."""
	available = {name: code for name, code in TARGET_LANGUAGES.items() if name != source_language}
	if not languages_arg:
		return available

	requested = [part.strip().lower() for part in languages_arg.split(",") if part.strip()]
	if not requested:
		print("Error: --languages was given but contained no language names.")
		return None

	selected = {}
	for name in requested:
		if name == source_language:
			print(f"Warning: '{name}' is the source language; skipping.")
			continue
		if name not in available:
			valid = ", ".join(sorted(available))
			print(f"Error: Unsupported target language '{name}'.")
			print(f"Supported values: {valid}")
			return None
		selected[name] = available[name]

	if not selected:
		print("Error: --languages selected no translatable languages.")
		return None
	return selected

def resolve_translate_targets(args, translate_workshop, translate_submods_default, translate_cn_default):
	"""Resolve whether to translate mod, workshop pages, submods, and change notes.

	``--submods`` widens the set of mods that get processed; it is not a target in its own
	right. On its own it therefore means "localization, for the main mod and every submod"
	rather than "nothing at all".
	"""
	if args.mod or args.workshop_pages or args.change_notes:
		# CLI target flags override config defaults for this run.
		return args.mod, args.workshop_pages, args.submods, args.change_notes
	if args.submods:
		return True, False, True, False
	# No flags: use config defaults (mod localization always on).
	return True, translate_workshop, translate_submods_default, translate_cn_default

def localization_base_paths(mod_root):
	"""Return every <mod_root>/<content root>/localization directory that exists."""
	paths = []
	for content_root in LOC_CONTENT_ROOTS:
		candidate = os.path.join(mod_root, content_root, "localization")
		if os.path.isdir(candidate):
			paths.append(candidate)
	return paths

def build_translation_targets(include_submods):
	"""Build translation targets for the main mod and optional submods."""
	targets = [
		{
			"cache_key": "main",
			"log_prefix": "",
			"mod_root": ROOT_DIR,
			"loc_base_paths": localization_base_paths(ROOT_DIR),
			"metadata_path": METADATA_PATH,
			"workshop_description_path": WORKSHOP_DESCRIPTION_PATH,
			"workshop_translations_dir": WORKSHOP_TRANSLATIONS_DIR,
			"workshop_template_path": WORKSHOP_TRANSLATION_TEMPLATE_PATH,
			"change_notes_path": CHANGE_NOTES_PATH,
			"change_notes_dir": CHANGE_NOTES_DIR
		}
	]

	if not include_submods:
		return targets

	if not os.path.isdir(SUBMODS_DIR):
		print(f"Warning: --submods specified, but directory not found: {SUBMODS_DIR}")
		return targets

	for entry in sorted(os.scandir(SUBMODS_DIR), key=lambda e: e.name.lower()):
		if not entry.is_dir():
			continue
		submod_root = entry.path
		workshop_dir = os.path.join(submod_root, "workshop")
		translations_dir = os.path.join(workshop_dir, "translations")
		targets.append(
			{
				"cache_key": entry.name,
				"log_prefix": f"[submods/{entry.name}] ",
				"mod_root": submod_root,
				"loc_base_paths": localization_base_paths(submod_root),
				"metadata_path": os.path.join(submod_root, ".metadata", "metadata.json"),
				"workshop_description_path": os.path.join(submod_root, "WORKSHOP_DESCRIPTION_steam.bbcode"),
				"workshop_translations_dir": translations_dir,
				"workshop_template_path": os.path.join(translations_dir, "translation_template.txt"),
				"change_notes_path": os.path.join(workshop_dir, "change-notes.bbcode"),
				"change_notes_dir": os.path.join(workshop_dir, "change_notes")
			}
		)

	return targets

def load_metadata_version(metadata_path):
	"""Read the mod version from metadata.json, or None when unavailable."""
	if not os.path.exists(metadata_path):
		return None
	try:
		with open(metadata_path, "r", encoding="utf-8-sig") as f:
			data = json.load(f)
	except Exception as e:
		print(f"Warning: Failed to read metadata file '{metadata_path}': {e}")
		return None
	version = data.get("version")
	version = str(version).strip() if version is not None else ""
	return version or None

def load_change_notes_source(change_notes_path, change_notes_dir, version):
	"""Resolve the change note text to translate.

	Prefers the per-version file at ``<change_notes_dir>/<version>.bbcode`` (what upload.py
	ships), falling back to the newest entry in the shared multi-version archive.
	"""
	if change_notes_dir and version:
		per_version_path = os.path.join(change_notes_dir, f"{version}.bbcode")
		text = load_workshop_description(per_version_path)
		if text and text.strip():
			# Drop a leading [h1] title line so the note matches upload.py's canonical shape.
			lines = text.strip().splitlines()
			if lines and re.match(r"^\[h1\].*\[/h1\]$", lines[0].strip()):
				lines = lines[1:]
			body = "\n".join(lines).strip()
			if body:
				return body

	raw = load_workshop_description(change_notes_path) if change_notes_path else None
	if raw is None or not raw.strip():
		return None
	entry = parse_change_notes_entry(raw, version=None)
	return entry if entry and entry.strip() else None

def get_cache_bucket(hash_data, cache_key):
	"""Return the hash/cache bucket for the main mod or a specific submod."""
	if cache_key == "main":
		files = hash_data.setdefault("files", {})
		if not isinstance(files, dict):
			hash_data["files"] = {}
		return hash_data

	submods_cache = hash_data.setdefault("submods", {})
	if not isinstance(submods_cache, dict):
		submods_cache = {}
		hash_data["submods"] = submods_cache

	cache_bucket = submods_cache.setdefault(cache_key, {})
	if not isinstance(cache_bucket, dict):
		cache_bucket = {}
		submods_cache[cache_key] = cache_bucket

	files = cache_bucket.setdefault("files", {})
	if not isinstance(files, dict):
		cache_bucket["files"] = {}

	return cache_bucket

def get_translator():
	"""Create a DeepL Translator instance, or None when DeepL is not configured/needed."""
	if deepl is None:
		return None
	if not AUTH_KEY:
		return None
	try:
		return deepl.Translator(AUTH_KEY)
	except Exception as e:
		print(f"Error initializing DeepL: {e}")
		return None

def require_deepl(selected_translators):
	"""Validate the DeepL dependency/key when any selected translator uses DeepL."""
	if "deepl" not in selected_translators:
		return True
	if deepl is None:
		print("Error: a 'deepl' translator is selected but the deepl package is not installed.")
		print("Install it with: pip install deepl")
		return False
	if not AUTH_KEY:
		print("Error: a 'deepl' translator is selected but DEEPL_API_KEY was not found in the environment/.env.")
		print("Please create a .env file with DEEPL_API_KEY=your_key_here")
		return False
	return True

# ==========================================
# LOCAL (OpenAI-COMPATIBLE) BACKEND
# ==========================================

def _local_chat(messages, max_tokens=None, json_object=False):
	"""POST a chat completion to the local OpenAI-compatible server, with retries."""
	model = LOCAL_SETTINGS.get("model")
	if not model:
		print("Error: local_model is not set in config.toml.")
		return None

	url = LOCAL_SETTINGS["api_base"].rstrip("/") + "/chat/completions"
	payload = {
		"model": model,
		"messages": messages,
		"temperature": LOCAL_SETTINGS["temperature"],
		"max_tokens": max_tokens or LOCAL_SETTINGS["max_tokens"],
		"stream": False,
	}
	if json_object:
		payload["response_format"] = {"type": "json_object"}
	if LOCAL_SETTINGS["disable_thinking"]:
		# llama.cpp/llama-swap forward this to the chat template; reasoning models
		# otherwise spend most of their token budget thinking about each string.
		payload["chat_template_kwargs"] = {"enable_thinking": False}

	headers = {"Content-Type": "application/json"}
	if LOCAL_SETTINGS["api_key"]:
		headers["Authorization"] = f"Bearer {LOCAL_SETTINGS['api_key']}"

	body = json.dumps(payload).encode("utf-8")
	max_attempts = 3
	base_delay = 2

	for attempt in range(1, max_attempts + 1):
		request = urllib.request.Request(url, data=body, headers=headers, method="POST")
		try:
			with urllib.request.urlopen(request, timeout=LOCAL_SETTINGS["timeout"]) as response:
				raw = response.read().decode("utf-8")
			data = json.loads(raw)
			choices = data.get("choices") or []
			if not choices:
				raise ValueError("response contained no choices")
			return choices[0].get("message", {}).get("content") or ""
		except Exception as e:
			if attempt < max_attempts:
				delay = base_delay * (2 ** (attempt - 1))
				print(f"  [Warning] Local API request failed ({e}) on attempt {attempt}/{max_attempts}. Retrying in {delay}s...")
				time.sleep(delay)
				continue
			print(f"  [Error] Local API request failed: {e}")
			return None

def markup_tokens(text):
	"""Return the multiset of markup tokens that must survive translation."""
	return MARKUP_TOKEN_RE.findall(text or "")

def missing_markup_tokens(source_text, translated_text):
	"""Return source markup tokens absent from the translated text."""
	missing = []
	remaining = translated_text or ""
	for token in markup_tokens(source_text):
		idx = remaining.find(token)
		if idx == -1:
			missing.append(token)
		else:
			# Consume the match so duplicated tokens must appear the same number of times.
			remaining = remaining[:idx] + remaining[idx + len(token):]
	return missing

def invented_markup_tokens(source_text, translated_text):
	"""Return markup tokens the translation added that the source never had.

	Models like to "help" by turning an English "they" into [minister.GetSheHe], or by
	inventing fragments like [e]. A scope that is not available for that key logs an error
	in-game, so any added token is rejected rather than trusted.
	"""
	source_tokens = set(markup_tokens(source_text))
	return sorted({t for t in markup_tokens(translated_text) if t not in source_tokens})

def markup_is_faithful(source_text, translated_text):
	"""True when the translation carries exactly the source's markup, nothing more or less."""
	return (
		not missing_markup_tokens(source_text, translated_text)
		and not invented_markup_tokens(source_text, translated_text)
	)

def _strip_code_fence(text):
	"""Remove a ```json ... ``` fence some models wrap JSON replies in."""
	stripped = (text or "").strip()
	if not stripped.startswith("```"):
		return stripped
	stripped = re.sub(r'^```[A-Za-z0-9_-]*\s*', '', stripped)
	if stripped.endswith("```"):
		stripped = stripped[:-3]
	return stripped.strip()

def _parse_json_object(text):
	"""Parse a JSON object from a model reply, tolerating fences and trailing prose."""
	candidate = _strip_code_fence(text)
	try:
		parsed = json.loads(candidate)
	except Exception:
		match = re.search(r'\{.*\}', candidate, flags=re.DOTALL)
		if not match:
			return None
		try:
			parsed = json.loads(match.group(0))
		except Exception:
			return None
	return parsed if isinstance(parsed, dict) else None

# Appended to every localization prompt. The engine resolves these tokens against scopes
# that only exist for a given key, so inventing one is a runtime error, not a style choice.
MARKUP_RULE = (
	"\n\nMarkup rules, which override any instinct to improve the text:"
	" [scope.Function] and [Concept('a','b')] links, $VARIABLE$ tokens, @icon! sprites,"
	" #colour ... #! blocks and literal \\n sequences must be reproduced character-for-character."
	" Reproduce exactly the tokens present in the source: never drop one, and never add one that"
	" is not already there. If the source says \"they\" with no token, translate it as ordinary"
	" words — do not substitute a pronoun token such as [minister.GetSheHe]."
)

def _build_local_batch_prompt(system_prompt, target_language, additional_context):
	"""Build the system prompt for a batched localization request."""
	prompt = _build_gemini_system_prompt(system_prompt, target_language, additional_context)
	return (
		prompt
		+ "\n\nYou will receive a JSON object mapping string ids to English source strings."
		" Translate every value and reply with ONLY a JSON object using the exact same ids."
		" Do not merge or split entries."
		+ MARKUP_RULE
	)

def _local_translate_chunk(values, target_language, system_prompt, additional_context):
	"""Translate one chunk of values; returns {source_value: translated_value} for successes."""
	items = {str(i): value for i, value in enumerate(values)}
	messages = [
		{"role": "system", "content": _build_local_batch_prompt(system_prompt, target_language, additional_context)},
		{"role": "user", "content": json.dumps(items, ensure_ascii=False, indent=1)},
	]
	content = _local_chat(messages, json_object=True)
	if content is None:
		return {}

	parsed = _parse_json_object(content)
	if parsed is None:
		print(f"  [Warning] Local API returned unparseable JSON for a batch of {len(values)}; falling back to per-string requests.")
		return {}

	results = {}
	for idx, value in items.items():
		translated = parsed.get(idx)
		if not isinstance(translated, str) or not translated.strip():
			continue
		translated = normalize_localization_linebreaks(translated)
		if not markup_is_faithful(value, translated):
			continue
		results[value] = cleanup_text(translated)
	return results

def _local_translate_single(value, target_language, system_prompt, additional_context):
	"""Translate a single value, used as the retry path for batch failures.

	Markup must come back intact. A first miss is retried with the required tokens spelled
	out; if the model still drops one we give up and return None, because reinserting a
	token (a mid-sentence pronoun link, say) at the end of the sentence produces text that
	reads as a bug. The caller keeps the English source instead.
	"""
	prompt = _build_gemini_system_prompt(system_prompt, target_language, additional_context)
	required = markup_tokens(value)

	for attempt in (1, 2):
		messages = [{"role": "system", "content": prompt + MARKUP_RULE}]
		if attempt == 2:
			messages[0]["content"] += (
				"\n\nThe previous attempt got the markup wrong. The translation must contain"
				" exactly these tokens, verbatim and in positions that read naturally"
				" — no others, none omitted: "
				+ (", ".join(required) if required else "(none at all)")
			)
		messages.append({"role": "user", "content": value})

		content = _local_chat(messages)
		if content is None:
			return None
		translated = normalize_localization_linebreaks(_strip_code_fence(content))
		if markup_is_faithful(value, translated):
			return cleanup_text(translated)
		problem = (
			f"dropped {missing_markup_tokens(value, translated)}"
			if missing_markup_tokens(value, translated)
			else f"invented {invented_markup_tokens(value, translated)}"
		)

	print(f"  [WARNING] {target_language}: {problem} after 2 attempts; "
	      f"keeping the English source for this string.")
	return None

def translate_values_local(values, target_folder_name, system_prompt, additional_context, log_prefix=""):
	"""Batch-translate many localization values against the local server.

	Values are chunked and dispatched concurrently. Any value the batch pass drops or
	mangles is retried on its own; values that still fail are left untranslated by the
	caller so the English source is preserved rather than corrupted.
	"""
	pending = [v for v in values if v]
	if not pending:
		return {}

	target_language = LANGUAGE_DISPLAY_NAMES.get(target_folder_name, target_folder_name)
	batch_size = max(1, LOCAL_SETTINGS["batch_size"])
	concurrency = max(1, LOCAL_SETTINGS["concurrency"])
	chunks = [pending[i:i + batch_size] for i in range(0, len(pending), batch_size)]

	results = {}
	started = time.time()
	done = 0
	print(f"{log_prefix}Translating {len(pending)} strings -> {target_folder_name} "
	      f"({len(chunks)} batches, concurrency {concurrency})...")

	def worker(chunk):
		return _local_translate_chunk(chunk, target_language, system_prompt, additional_context)

	with ThreadPoolExecutor(max_workers=concurrency) as executor:
		for chunk, chunk_results in zip(chunks, executor.map(worker, chunks)):
			results.update(chunk_results)
			done += len(chunk)
			elapsed = time.time() - started
			rate = done / elapsed if elapsed > 0 else 0
			remaining = (len(pending) - done) / rate if rate > 0 else 0
			print(f"{log_prefix}  {done}/{len(pending)} -> {target_folder_name} "
			      f"({rate:.2f} str/s, ~{remaining / 60:.0f} min left)")

	retries = [v for v in pending if v not in results]
	if retries:
		print(f"{log_prefix}  Retrying {len(retries)} strings individually -> {target_folder_name}...")
		def retry_worker(value):
			return value, _local_translate_single(value, target_language, system_prompt, additional_context)
		with ThreadPoolExecutor(max_workers=concurrency) as executor:
			for value, translated in executor.map(retry_worker, retries):
				if translated:
					results[value] = translated
		still_failed = [v for v in retries if v not in results]
		if still_failed:
			print(f"{log_prefix}  [WARNING] {len(still_failed)} strings could not be translated to "
			      f"{target_folder_name}; leaving the English source in place.")

	return results

def translate_text_local(text, target_folder_name, system_prompt, additional_context):
	"""Translate a free-form block (workshop title/description/change notes) locally."""
	if text == "":
		return ""
	target_language = LANGUAGE_DISPLAY_NAMES.get(target_folder_name, target_folder_name)
	prompt = _build_gemini_system_prompt(system_prompt, target_language, additional_context)
	content = _local_chat([
		{"role": "system", "content": prompt},
		{"role": "user", "content": text},
	])
	if content is None:
		return None
	translated = _strip_code_fence(content)
	if text.endswith("\n") and not translated.endswith("\n"):
		translated += "\n"
	return translated

# ==========================================
# BATCH COLLECTION STATE
# ==========================================

class BatchState:
	"""Two-pass batching state for the local backend.

	Pass 1 runs the normal file walk with ``collecting`` set, which records every value
	that would be translated without writing anything. The recorded values are then
	translated in batches, and pass 2 re-runs the walk reading translations from ``memo``.
	"""

	def __init__(self):
		self.enabled = False
		self.collecting = False
		self.pending = {}
		self.memo = {}

	def reset_pending(self):
		self.pending = {}

	def record(self, language, value):
		self.pending.setdefault(language, set()).add(value)

	def lookup(self, language, value):
		return self.memo.get((language, value))

	def store(self, language, results):
		for source, translated in results.items():
			self.memo[(language, source)] = translated

	def flush(self, system_prompt, additional_context, log_prefix=""):
		"""Translate everything recorded during the collect pass."""
		for language in sorted(self.pending):
			values = sorted(v for v in self.pending[language] if (language, v) not in self.memo)
			if not values:
				continue
			results = translate_values_local(values, language, system_prompt, additional_context, log_prefix)
			self.store(language, results)
		self.reset_pending()

BATCH = BatchState()

def load_hashes(path):
	"""
	Load the per-file, per-key hash cache. If missing or invalid, rebuild cleanly.
	"""
	if not os.path.exists(path):
		return {"version": HASH_FILE_VERSION, "files": {}}

	try:
		with open(path, "r", encoding="utf-8") as f:
			data = json.load(f)
		if not isinstance(data, dict):
			raise ValueError("Hash file must be a JSON object.")
		if data.get("version") != HASH_FILE_VERSION:
			raise ValueError("Unsupported hash file version.")
		files = data.get("files")
		if not isinstance(files, dict):
			raise ValueError("Hash file 'files' must be a JSON object.")
		return data
	except Exception as e:
		print(f"Warning: Failed to read hash file '{path}': {e}. Rebuilding.")
		return {"version": HASH_FILE_VERSION, "files": {}}

def save_hashes(path, data):
	"""
	Atomically persist the hash cache to disk.
	"""
	os.makedirs(os.path.dirname(path), exist_ok=True)
	tmp_path = path + ".tmp"
	with open(tmp_path, "w", encoding="utf-8") as f:
		json.dump(data, f, indent=2, sort_keys=True)
	os.replace(tmp_path, path)

def hash_text(text):
	"""
	Stable hash of the source value to detect changes.
	"""
	return hashlib.sha256(text.encode("utf-8")).hexdigest()

def mask_text_var(text):
	"""
	Replaces blocks with [VAR_0], [VAR_1], etc to prevent DeepL from breaking it.
	"""
	placeholders = []

	def replace_match(match):
		idx = len(placeholders)
		placeholders.append(match.group(0))
		return f'[VAR_{idx}]'

	# Single pass prevents already-masked [VAR_x] tokens from being re-masked.
	pattern = re.compile(
		r'(\\n|\[.*?\]|\$.*?\$|@[a-zA-Z0-9_]+!?|#[a-zA-Z0-9_]+|#!)'
	)
	text = pattern.sub(replace_match, text)

	return text, placeholders

def escape_xml(text):
	"""Escape XML special chars so DeepL XML tag handling stays valid."""
	return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def unescape_xml(text):
	"""Reverse escape_xml using standard HTML entity unescape."""
	return html.unescape(text)

def mask_text_var_xml_from_masked(masked_text, placeholders):
	"""Convert [VAR_x] placeholders into XML tags for DeepL tag handling."""
	escaped = escape_xml(masked_text)
	def replace_match(match):
		try:
			idx = int(match.group(1))
			placeholder_text = placeholders[idx]
		except (ValueError, IndexError):
			placeholder_text = match.group(0)
		return f'<{XML_PLACEHOLDER_TAG} id="{match.group(1)}">{escape_xml(placeholder_text)}</{XML_PLACEHOLDER_TAG}>'
	return re.sub(r'\[VAR_(\d+)\]', replace_match, escaped)

def unmask_text_var(text, placeholders):
	"""
	Restores [VAR_0] -> Original Text.
	"""
	def restore_match(match):
		try:
			idx = int(match.group(1))
			if 0 <= idx < len(placeholders):
				return placeholders[idx]
		except ValueError:
			pass
		return match.group(0)

	# Regex matches: Optional [, whitespace, VAR_, Digit, whitespace, Optional ]
	return re.sub(r'\[?\s*VAR_(\d+)\s*\]?', restore_match, text)

def unmask_text_var_xml(text, placeholders):
	"""
	Restores <locvar id="0">...</locvar> -> Original Text.
	"""
	def restore_match(match):
		try:
			idx = int(match.group(1))
			if 0 <= idx < len(placeholders):
				return placeholders[idx]
		except ValueError:
			pass
		return match.group(0)

	# Replace paired tags with or without content.
	text = re.sub(
		rf'<{XML_PLACEHOLDER_TAG}\s+id=[\'"](\d+)[\'"]\s*>.*?</{XML_PLACEHOLDER_TAG}\s*>',
		restore_match,
		text,
		flags=re.DOTALL
	)
	# Replace self-closing tags.
	return re.sub(
		rf'<{XML_PLACEHOLDER_TAG}\s+id=[\'"](\d+)[\'"]\s*/\s*>',
		restore_match,
		text
	)

def normalize_localization_linebreaks(text):
	"""Convert raw line breaks to escaped \\n for single-line localization values."""
	text = text.replace("\r\n", "\n").replace("\r", "\n")
	return text.replace("\n", r"\n")

def missing_placeholder_indices(translated_text, placeholders):
	"""Return indices of placeholders missing from translated_text (VAR or XML-tagged)."""
	found_set = set(int(x) for x in re.findall(r'VAR_(\d+)', translated_text))
	found_set.update(
		int(x)
		for x in re.findall(rf'<{XML_PLACEHOLDER_TAG}\s+id=[\'"](\d+)[\'"]', translated_text)
	)

	missing = []
	for i, placeholder in enumerate(placeholders):
		if i in found_set:
			continue
		if placeholder == r"\n" and "\n" in translated_text:
			continue
		if placeholder and placeholder in translated_text:
			continue
		missing.append(i)
	return missing

def insert_missing_placeholders(text, placeholders, missing_indices):
	"""Append missing placeholders, keeping punctuation at the end if possible."""
	if not missing_indices:
		return text
	missing_tokens = [placeholders[i] for i in missing_indices]
	suffix = "".join(missing_tokens)
	if not text:
		return suffix

	match = re.search(r'([.!?。！？])\s*$', text)
	if match:
		# Keep sentence-ending punctuation last to avoid odd UI output.
		idx = match.start(1)
		return text[:idx] + suffix + text[idx:]
	return text + suffix

def translate_deepl_xml(translator, masked_text, placeholders, deepl_code, source_lang_deepl, split_sentences):
	"""Translate masked text using XML tag handling."""
	masked_xml = mask_text_var_xml_from_masked(masked_text, placeholders)
	result = translator.translate_text(
		masked_xml,
		target_lang=deepl_code,
		source_lang=source_lang_deepl,
		tag_handling="xml",
		non_splitting_tags=[XML_PLACEHOLDER_TAG],
		ignore_tags=[XML_PLACEHOLDER_TAG],
		split_sentences=split_sentences,
		preserve_formatting=True
	)
	translated_raw = normalize_localization_linebreaks(unescape_xml(result.text))
	missing = missing_placeholder_indices(translated_raw, placeholders)
	translated_text = unmask_text_var_xml(translated_raw, placeholders)
	translated_text = unmask_text_var(translated_text, placeholders)
	return translated_text, missing

def translate_deepl_plain(translator, masked_text, placeholders, deepl_code, source_lang_deepl, split_sentences):
	"""Translate masked text without XML tag handling."""
	result = translator.translate_text(
		masked_text,
		target_lang=deepl_code,
		source_lang=source_lang_deepl,
		split_sentences=split_sentences,
		preserve_formatting=True
	)
	translated_raw = normalize_localization_linebreaks(result.text)
	missing = missing_placeholder_indices(translated_raw, placeholders)
	translated_text = unmask_text_var(translated_raw, placeholders)
	return translated_text, missing

def validate_translation(translated_text, placeholders):
	"""
	Checks if DeepL dropped any tags.
	"""
	missing_indices = missing_placeholder_indices(translated_text, placeholders)

	if missing_indices:
		missing_tags = [placeholders[i] for i in missing_indices]
		return False, f"Missing tags: {missing_tags}"

	return True, "OK"

def cleanup_text(text):
	"""
	Cleans up common AI formatting errors.
	"""
	text = re.sub(r'\s+([,.])', r'\1', text) # Fix space before punctuation
	text = re.sub(r' +', ' ', text)          # Fix double spaces
	text = text.replace('[[', '[').replace(']]', ']') # Fix double brackets
	return text.strip()

def should_auto_skip(masked_text):
	"""
	Returns True if the line should be skipped.
	Conditions:
	1. Line is empty or whitespace.
	2. Line consists only of placeholders and punctuation (e.g., "[VAR_0]").
	"""
	# 1. Check for empty/whitespace only
	if not masked_text.strip():
		return True

	# 2. Remove all [VAR_x] tags
	stripped = re.sub(r'\[VAR_\d+\]', '', masked_text)

	# 3. Remove standard punctuation and whitespace
	stripped = re.sub(r'[ \t\.,!?:;]', '', stripped)

	# If nothing is left, it was only placeholders/punctuation
	return len(stripped) == 0

def parse_source_entries(lines):
	"""
	Parse all translatable key/value entries with NO-TRANSLATE flags.
	"""
	entries = []
	ignore_block_active = False

	for line in lines:
		if "# NO-TRANSLATE BELOW" in line:
			ignore_block_active = True
		if "# NO-TRANSLATE END" in line:
			ignore_block_active = False

		no_translate = ignore_block_active or ("# NO-TRANSLATE" in line)

		match = KEY_VALUE_RE.match(line)
		if match:
			indent = match.group(1)
			key = match.group(2)
			original_value = match.group(3)
			comment = match.group(4) if match.group(4) else ""
			# Skip self-referential keys (key == value)
			self_ref = (key.strip() == original_value)
			entries.append({
				"indent": indent,
				"key": key,
				"value": original_value,
				"comment": comment,
				"no_translate": no_translate or self_ref
			})

	return entries

def translate_localization_value_gemini(
	masked_text,
	placeholders,
	target_language,
	key,
	target_folder_name,
	system_prompt,
	additional_context=""
):
	"""Translate a single localization value using Gemini."""
	prompt = _build_gemini_system_prompt(system_prompt, target_language, additional_context)
	payload = {
		"systemInstruction": {"parts": [{"text": prompt}]},
		"contents": [
			{"role": "user", "parts": [{"text": masked_text}]}
		]
	}

	response = _gemini_generate_content(payload)
	if response is None:
		return None

	translated_text = _gemini_extract_text(response)
	if translated_text is None:
		print("  [Error] Gemini API returned no text.")
		return None

	translated_text = normalize_localization_linebreaks(translated_text)
	missing = missing_placeholder_indices(translated_text, placeholders)
	if missing:
		missing_tags = [placeholders[i] for i in missing]
		print(f"  [WARNING] {target_folder_name} issue in '{key}': Missing tags: {missing_tags}")
		translated_text = insert_missing_placeholders(translated_text, placeholders, missing)

	translated_text = unmask_text_var(translated_text, placeholders)
	return cleanup_text(translated_text)

def translate_value(
	translator,
	key,
	original_value,
	deepl_code,
	source_lang_deepl,
	target_folder_name,
	no_translate,
	localization_translator,
	gemini_localization_system_prompt,
	gemini_additional_context=""
):
	"""
	Translate a single value with tag masking and validation.
	"""
	if no_translate:
		return original_value

	masked_text, placeholders = mask_text_var(original_value)

	if should_auto_skip(masked_text):
		return original_value

	if localization_translator == LOCAL_TRANSLATOR:
		# The local backend translates raw (unmasked) text: instruct models keep markup
		# intact and read it as context, and every result is markup-validated anyway.
		if BATCH.collecting:
			BATCH.record(target_folder_name, original_value)
			return original_value
		cached = BATCH.lookup(target_folder_name, original_value)
		if cached is not None:
			return cached
		translated_text = _local_translate_single(
			original_value,
			LANGUAGE_DISPLAY_NAMES.get(target_folder_name, target_folder_name),
			gemini_localization_system_prompt,
			gemini_additional_context
		)
		if translated_text is None:
			print(f"  [Error] Failed to translate line: {key} (local request failed)")
			return original_value
		BATCH.store(target_folder_name, {original_value: translated_text})
		return translated_text

	if localization_translator == "gemini-3-flash":
		target_language = LANGUAGE_DISPLAY_NAMES.get(target_folder_name, target_folder_name)
		translated_text = translate_localization_value_gemini(
			masked_text,
			placeholders,
			target_language,
			key,
			target_folder_name,
			gemini_localization_system_prompt,
			gemini_additional_context
		)
		if translated_text is None:
			print(f"  [Error] Failed to translate line: {key} (Gemini request failed)")
			return original_value
		return translated_text

	try:
		split_sentences = deepl_split_sentences_off() if placeholders else None

		translated_text, missing_xml = translate_deepl_xml(
			translator,
			masked_text,
			placeholders,
			deepl_code,
			source_lang_deepl,
			split_sentences
		)

		translated_plain = None
		missing_plain = None
		if missing_xml:
			translated_plain, missing_plain = translate_deepl_plain(
				translator,
				masked_text,
				placeholders,
				deepl_code,
				source_lang_deepl,
				split_sentences
			)

		# Choose the translation that preserves more placeholders.
		if missing_plain is not None and len(missing_plain) < len(missing_xml):
			translated_text = translated_plain
			missing = missing_plain
		else:
			missing = missing_xml

		if missing:
			missing_tags = [placeholders[i] for i in missing]
			print(f"  [WARNING] {target_folder_name} issue in '{key}': Missing tags: {missing_tags}")
			# If the engine drops tags, reinsert them rather than falling back to English.
			translated_text = insert_missing_placeholders(translated_text, placeholders, missing)

		translated_text = cleanup_text(translated_text)
		return translated_text

	except Exception as e:
		print(f"  [Error] Failed to translate line: {key} ({e})")
		return original_value

def build_line(indent, key, text, comment):
	"""Format a localization key/value line with optional comment."""
	return f'{indent}{key}: "{text}"{comment}\n'

def is_locked_line(line):
	"""
	Detect a # LOCK comment on an output line to prevent overwrites.
	"""
	match = KEY_VALUE_RE.match(line)
	if not match:
		return False
	comment = match.group(4) if match.group(4) else ""
	return bool(LOCK_RE.search(comment))

def ensure_target_header(target_lines, new_lang_id):
	"""
	Ensure the localization header matches the target language.
	"""
	for i, line in enumerate(target_lines):
		if HEADER_RE.match(line.strip()):
			if line.strip() != f"{new_lang_id}:":
				target_lines[i] = f"{new_lang_id}:\n"
				return True
			return False
	return False

def build_target_key_index(lines):
	"""
	Build a key->line index for fast in-place updates.
	"""
	index = {}
	for i, line in enumerate(lines):
		match = KEY_VALUE_RE.match(line)
		if match:
			index[match.group(2)] = i
	return index

def prune_target_lines(target_lines, source_keys):
	"""Remove translated lines whose keys no longer exist in the source."""
	new_lines = []
	removed_count = 0
	for line in target_lines:
		match = KEY_VALUE_RE.match(line)
		if match and match.group(2) not in source_keys:
			removed_count += 1
			continue
		new_lines.append(line)
	return new_lines, removed_count

def update_target_lines(
	translator,
	target_lines,
	source_entries,
	changed_keys,
	deepl_code,
	source_lang_deepl,
	target_folder_name,
	localization_translator,
	gemini_localization_system_prompt,
	gemini_additional_context=""
):
	"""
	Update only keys that changed in the source (or are missing in the target).
	"""
	target_index = build_target_key_index(target_lines)
	file_changed = False

	for entry in source_entries:
		key = entry["key"]

		needs_update = key in changed_keys or key not in target_index
		if not needs_update:
			continue

		translated_text = translate_value(
			translator,
			key,
			entry["value"],
			deepl_code,
			source_lang_deepl,
			target_folder_name,
			entry["no_translate"],
			localization_translator,
			gemini_localization_system_prompt,
			gemini_additional_context
		)

		if key in target_index:
			line_index = target_index[key]
			existing_line = target_lines[line_index]
			if is_locked_line(existing_line):
				continue
			match = KEY_VALUE_RE.match(existing_line)
			if match:
				indent = match.group(1)
				comment = match.group(4) if match.group(4) else ""
				new_line = build_line(indent, key, translated_text, comment)
			else:
				new_line = build_line(entry["indent"], key, translated_text, entry["comment"])

			if new_line != existing_line:
				target_lines[line_index] = new_line
				file_changed = True
		else:
			new_line = build_line(entry["indent"], key, translated_text, entry["comment"])
			if target_lines and not target_lines[-1].endswith("\n"):
				target_lines[-1] = target_lines[-1] + "\n"
			target_lines.append(new_line)
			target_index[key] = len(target_lines) - 1
			file_changed = True

	return file_changed

def translate_source_lines(
	translator,
	source_lines,
	target_folder_name,
	deepl_code,
	source_lang_id,
	source_lang_deepl,
	localization_translator,
	gemini_localization_system_prompt,
	gemini_additional_context=""
):
	"""
	Translate a full source file into a new target file.
	"""
	new_lang_id = f"l_{target_folder_name}"
	new_lines = []
	ignore_block_active = False

	for line in source_lines:
		stripped_line = line.strip()

		# 1. Handle Language Header
		if stripped_line.startswith(f"{source_lang_id}:"):
			new_lines.append(f"{new_lang_id}:\n")
			continue

		# 2. Check for ignored lines
		if "# NO-TRANSLATE BELOW" in line:
			ignore_block_active = True
			new_lines.append(line)
			continue

		if "# NO-TRANSLATE END" in line:
			ignore_block_active = False
			new_lines.append(line)
			continue

		if ignore_block_active:
			new_lines.append(line)
			continue

		if "# NO-TRANSLATE" in line:
			new_lines.append(line)
			continue

		# 3. Parse Key-Value Pairs
		match = KEY_VALUE_RE.match(line)

		if match:
			indent = match.group(1)
			key = match.group(2)
			original_value = match.group(3)
			comment = match.group(4) if match.group(4) else ""
			self_ref = (key.strip() == original_value)

			translated_text = translate_value(
				translator,
				key,
				original_value,
				deepl_code,
				source_lang_deepl,
				target_folder_name,
				self_ref,
				localization_translator,
				gemini_localization_system_prompt,
				gemini_additional_context
			)

			new_lines.append(build_line(indent, key, translated_text, comment))
		else:
			# Copy comments / whitespace lines
			new_lines.append(line)

	return new_lines

def process_file(
	translator,
	source_lines,
	source_entries,
	source_filepath,
	loc_base_path,
	target_folder_name,
	deepl_code,
	source_lang_id,
	source_lang_deepl,
	changed_keys,
	localization_translator,
	gemini_localization_system_prompt,
	gemini_additional_context,
	log_prefix
):
	"""Translate/update one localization file for a single target language."""
	filename = os.path.basename(source_filepath)
	new_lang_id = f"l_{target_folder_name}"
	if source_lang_id in filename:
		new_filename = filename.replace(source_lang_id, new_lang_id)
	else:
		new_filename = filename

	target_dir = os.path.join(loc_base_path, target_folder_name)
	if not BATCH.collecting:
		os.makedirs(target_dir, exist_ok=True)
	target_filepath = os.path.join(target_dir, new_filename)

	# If the target doesn't exist yet, write a fully translated file.
	if not os.path.exists(target_filepath):
		if not BATCH.collecting:
			print(f"{log_prefix}Translating {filename} -> {target_folder_name}...")
		new_lines = translate_source_lines(
			translator,
			source_lines,
			target_folder_name,
			deepl_code,
			source_lang_id,
			source_lang_deepl,
			localization_translator,
			gemini_localization_system_prompt,
			gemini_additional_context
		)
		if BATCH.collecting:
			return
		with open(target_filepath, 'w', encoding='utf-8-sig') as f:
			f.writelines(new_lines)
		return

	with open(target_filepath, 'r', encoding='utf-8-sig') as f:
		target_lines = f.readlines()

	target_index = build_target_key_index(target_lines)
	source_keys = {entry["key"] for entry in source_entries}
	has_missing_keys = any(entry["key"] not in target_index for entry in source_entries)
	has_removed_keys = any(key not in source_keys for key in target_index)
	header_needs_update = False
	for line in target_lines:
		if HEADER_RE.match(line.strip()):
			header_needs_update = line.strip() != f"{new_lang_id}:"
			break

	# Skip work if nothing changed and the header matches.
	if not changed_keys and not has_missing_keys and not has_removed_keys and not header_needs_update:
		if not BATCH.collecting:
			print(f"{log_prefix}No changes for {filename} -> {target_folder_name}; skipping.")
		return

	if not BATCH.collecting:
		print(f"{log_prefix}Translating {filename} -> {target_folder_name}...")

	# Update only changed or missing keys; preserve everything else.
	file_changed = ensure_target_header(target_lines, new_lang_id)
	if has_removed_keys:
		target_lines, removed_count = prune_target_lines(target_lines, source_keys)
		if removed_count:
			file_changed = True
			if not BATCH.collecting:
				print(f"{log_prefix}  Removed {removed_count} obsolete keys from {filename} -> {target_folder_name}.")
	file_changed = update_target_lines(
		translator,
		target_lines,
		source_entries,
		changed_keys,
		deepl_code,
		source_lang_deepl,
		target_folder_name,
		localization_translator,
		gemini_localization_system_prompt,
		gemini_additional_context
	) or file_changed

	if BATCH.collecting:
		return

	if file_changed:
		with open(target_filepath, 'w', encoding='utf-8-sig') as f:
			f.writelines(target_lines)
	else:
		print(f"{log_prefix}No output changes for {filename} -> {target_folder_name}.")

def _remove_dev_suffix(name):
	"""Strip a trailing ' Dev' suffix from a mod name."""
	if name.endswith(" Dev"):
		return name[:-4].rstrip()
	return name.strip()

def load_workshop_title(metadata_path):
	"""Load the workshop title from metadata.json and remove dev suffix."""
	if not os.path.exists(metadata_path):
		return None
	try:
		with open(metadata_path, "r", encoding="utf-8-sig") as f:
			data = json.load(f)
	except Exception as e:
		print(f"Warning: Failed to read metadata file '{metadata_path}': {e}")
		return None

	title = data.get("name")
	if not title:
		print(f"Warning: Metadata 'name' not found in {metadata_path}")
		return None

	return _remove_dev_suffix(str(title))

def load_workshop_description(description_path):
	"""Read the workshop description source text."""
	if not os.path.exists(description_path):
		return None
	try:
		with open(description_path, "r", encoding="utf-8-sig") as f:
			return f.read()
	except Exception as e:
		print(f"Warning: Failed to read workshop description '{description_path}': {e}")
		return None

def split_workshop_description(text):
	"""Split workshop description into translatable and source variants."""
	if text is None:
		return None, None
	lines = text.splitlines(keepends=True)
	for idx, line in enumerate(lines):
		if line.strip() == WORKSHOP_NO_TRANSLATE_BELOW:
			translatable = "".join(lines[:idx])
			source_text = "".join(lines[:idx] + lines[idx + 1:])
			return translatable, source_text
	return text, text

def apply_workshop_item_id(text, item_id):
	"""Replace the $item-id$ token when an item id is available."""
	if text is None or item_id is None:
		return text
	return text.replace(WORKSHOP_ITEM_ID_TOKEN, str(item_id))

def parse_change_notes_entry(text, version=None):
	"""Extract a single versioned entry from change notes text.

	If version is None, returns the latest (topmost) entry body.
	Returns None if no version headers are found or no entry matches the requested version.
	The translate tool always returns only the body (no version header).
	"""
	entries = []
	current_version = None
	current_lines = []

	for line in text.splitlines(keepends=True):
		m = CHANGE_NOTES_VERSION_RE.match(line.strip())
		if m:
			if current_version is not None:
				entries.append((current_version, "".join(current_lines).strip()))
			current_version = m.group(2).strip()
			current_lines = []
		elif current_version is not None:
			current_lines.append(line)

	if current_version is not None:
		entries.append((current_version, "".join(current_lines).strip()))

	if not entries:
		return None

	if version is None:
		return entries[0][1] or None

	for entry_version, content in entries:
		if entry_version == version:
			return content or None

	return None

def build_workshop_translation_text(title, description):
	"""Build the combined workshop translation file content."""
	parts = []
	if title is not None:
		parts.append(f"{WORKSHOP_TITLE_MARKER}\n{title}\n")
	if description is not None:
		parts.append(f"{WORKSHOP_DESCRIPTION_MARKER}\n{description}")
	return "".join(parts)

def load_workshop_translation_template(template_path):
	"""Load the translation template text if present and valid."""
	if not os.path.exists(template_path):
		return None
	try:
		with open(template_path, "r", encoding="utf-8") as f:
			template = f.read()
	except Exception as e:
		print(f"Warning: Failed to read workshop translation template '{template_path}': {e}")
		return None

	if WORKSHOP_TITLE_MARKER not in template or WORKSHOP_DESCRIPTION_MARKER not in template:
		print(f"Warning: Workshop translation template '{template_path}' is missing required markers; ignoring it.")
		return None

	return template

def resolve_workshop_translation_template(primary_template_path, fallback_template_path):
	"""Load workshop template, falling back to fallback_template_path when needed."""
	template = load_workshop_translation_template(primary_template_path)
	if template is not None:
		return template

	primary_norm = os.path.normcase(os.path.normpath(primary_template_path))
	fallback_norm = os.path.normcase(os.path.normpath(fallback_template_path))
	if primary_norm == fallback_norm:
		return None

	return load_workshop_translation_template(fallback_template_path)

def render_workshop_translation_text(
	template,
	translated_title,
	translated_description,
	original_title,
	original_description,
	translated_language,
	original_language
):
	"""Render output using the template (or default format if missing)."""
	if not template:
		return build_workshop_translation_text(translated_title, translated_description)

	# Tokens are optional; missing values become empty strings.
	replacements = {
		"$Translated-Title$": translated_title or "",
		"$Original-Title$": original_title or "",
		"$Translated-Language$": translated_language or "",
		"$Original-Language$": original_language or "",
		"$Translated-Description$": translated_description or "",
		"$Original-Description$": original_description or ""
	}
	output = template
	for token, value in replacements.items():
		output = output.replace(token, value)
	return output

def translate_workshop_title(translator, title, deepl_code, source_lang_deepl):
	"""Translate the workshop title using DeepL."""
	try:
		result = translator.translate_text(
			title,
			target_lang=deepl_code,
			source_lang=source_lang_deepl
		)
		return cleanup_text(result.text)
	except Exception as e:
		print(f"  [Error] Failed to translate workshop title to {deepl_code}: {e}")
		return None

def translate_workshop_title_gemini(text, target_language, system_prompt, additional_context=""):
	"""Translate the workshop title using Gemini."""
	if text == "":
		return ""
	prompt = _build_gemini_system_prompt(system_prompt, target_language, additional_context)
	payload = {
		"systemInstruction": {"parts": [{"text": prompt}]},
		"contents": [
			{"role": "user", "parts": [{"text": text}]}
		]
	}

	response = _gemini_generate_content(payload)
	if response is None:
		return None

	translated_text = _gemini_extract_text(response)
	if translated_text is None:
		print("  [Error] Gemini API returned no text.")
		return None

	return cleanup_text(translated_text)

def translate_workshop_description(translator, text, deepl_code, source_lang_deepl):
	"""Translate the full workshop description using DeepL."""
	if text == "":
		return ""
	try:
		result = translator.translate_text(
			text,
			target_lang=deepl_code,
			source_lang=source_lang_deepl
		)
		translated_text = result.text
		if text.endswith("\n") and not translated_text.endswith("\n"):
			translated_text += "\n"
		return translated_text
	except Exception as e:
		print(f"  [Error] Failed to translate workshop description to {deepl_code}: {e}")
		return None

def _build_gemini_system_prompt(template, target_language, additional_context=""):
	"""Fill the {target_language} placeholder in the system prompt and append additional context."""
	try:
		prompt = template.format(target_language=target_language)
	except Exception:
		prompt = template
	if additional_context:
		prompt += "\n\nAdditional context: " + additional_context
	return prompt

def _gemini_generate_content(payload):
	"""Call the Gemini generateContent API with retries."""
	if not GEMINI_API_KEY:
		print("Error: GEMINI_API_KEY not found in .env file.")
		print("Please create a .env file with GEMINI_API_KEY=your_key_here")
		return None

	url = f"{GEMINI_API_BASE}/{GEMINI_MODEL}:generateContent"
	query = urllib.parse.urlencode({"key": GEMINI_API_KEY})
	request_body = json.dumps(payload).encode("utf-8")

	max_attempts = 3
	base_delay = 2

	# Retry transient failures with exponential backoff.
	for attempt in range(1, max_attempts + 1):
		request = urllib.request.Request(
			f"{url}?{query}",
			data=request_body,
			headers={"Content-Type": "application/json"},
			method="POST"
		)

		try:
			with urllib.request.urlopen(request, timeout=60) as response:
				raw = response.read().decode("utf-8")
			return json.loads(raw)
		except urllib.error.HTTPError as e:
			body = e.read().decode("utf-8", errors="ignore")
			retryable = e.code in (429, 500, 502, 503, 504)
			if retryable and attempt < max_attempts:
				delay = base_delay * (2 ** (attempt - 1))
				print(f"  [Warning] Gemini API request failed ({e.code}) on attempt {attempt}/{max_attempts}. Retrying in {delay}s...")
				time.sleep(delay)
				continue
			print(f"  [Error] Gemini API request failed ({e.code}): {body}")
			return None
		except urllib.error.URLError as e:
			if attempt < max_attempts:
				delay = base_delay * (2 ** (attempt - 1))
				print(f"  [Warning] Gemini API request failed ({e.reason}) on attempt {attempt}/{max_attempts}. Retrying in {delay}s...")
				time.sleep(delay)
				continue
			print(f"  [Error] Gemini API request failed: {e}")
			return None
		except Exception as e:
			if attempt < max_attempts:
				delay = base_delay * (2 ** (attempt - 1))
				print(f"  [Warning] Gemini API request failed ({e}) on attempt {attempt}/{max_attempts}. Retrying in {delay}s...")
				time.sleep(delay)
				continue
			print(f"  [Error] Gemini API request failed: {e}")
			return None

def _gemini_extract_text(response):
	"""Extract concatenated text from a Gemini response payload."""
	candidates = response.get("candidates") if isinstance(response, dict) else None
	if not candidates:
		return None
	content = candidates[0].get("content", {})
	parts = content.get("parts", []) if isinstance(content, dict) else []
	text_chunks = []
	for part in parts:
		text = part.get("text")
		if text:
			text_chunks.append(text)
	return "".join(text_chunks) if text_chunks else None

def translate_workshop_description_gemini(text, target_language, system_prompt, additional_context=""):
	"""Translate the full workshop description using Gemini."""
	if text == "":
		return ""
	prompt = _build_gemini_system_prompt(system_prompt, target_language, additional_context)
	payload = {
		"systemInstruction": {"parts": [{"text": prompt}]},
		"contents": [
			{"role": "user", "parts": [{"text": text}]}
		]
	}

	response = _gemini_generate_content(payload)
	if response is None:
		return None

	translated_text = _gemini_extract_text(response)
	if translated_text is None:
		print("  [Error] Gemini API returned no text.")
		return None

	if text.endswith("\n") and not translated_text.endswith("\n"):
		translated_text += "\n"
	return translated_text

def provider_label(provider):
	"""Human-readable provider name for progress output."""
	return provider if provider in ALLOWED_LOCALIZATION_TRANSLATORS else "deepl"

def dispatch_title_translation(provider, translator, text, folder_name, deepl_code,
                               source_lang_deepl, gemini_prompt, additional_context):
	"""Translate a workshop title with whichever provider is configured."""
	if provider == LOCAL_TRANSLATOR:
		translated = translate_text_local(text, folder_name, gemini_prompt, additional_context)
		return cleanup_text(translated) if translated is not None else None
	if provider == "gemini-3-flash":
		return translate_workshop_title_gemini(
			text, LANGUAGE_DISPLAY_NAMES.get(folder_name, folder_name), gemini_prompt, additional_context
		)
	return translate_workshop_title(translator, text, deepl_code, source_lang_deepl)

def dispatch_block_translation(provider, translator, text, folder_name, deepl_code,
                               source_lang_deepl, gemini_prompt, additional_context):
	"""Translate a free-form block (description / change notes) with the configured provider."""
	if provider == LOCAL_TRANSLATOR:
		return translate_text_local(text, folder_name, gemini_prompt, additional_context)
	if provider == "gemini-3-flash":
		return translate_workshop_description_gemini(
			text, LANGUAGE_DISPLAY_NAMES.get(folder_name, folder_name), gemini_prompt, additional_context
		)
	return translate_workshop_description(translator, text, deepl_code, source_lang_deepl)

def translate_workshop_assets(
	translator,
	source_language,
	source_lang_deepl,
	cache_bucket,
	workshop_description_translator,
	gemini_description_system_prompt,
	workshop_title_translator,
	gemini_title_system_prompt,
	gemini_additional_context,
	workshop_item_id,
	metadata_path,
	workshop_description_path,
	workshop_translations_dir,
	workshop_template_path,
	main_workshop_template_path,
	change_notes_path,
	change_notes_dir,
	mod_version,
	target_languages,
	log_prefix,
	translate_pages=True
):
	"""Translate workshop titles/descriptions and/or change notes."""
	title = None
	description = None
	translation_template = None

	if translate_pages:
		has_description_file = os.path.exists(workshop_description_path)
		if not has_description_file:
			print(f"{log_prefix}Workshop description not found: {workshop_description_path}; skipping workshop page translations.")
			return False

		title = load_workshop_title(metadata_path)
		raw_description = load_workshop_description(workshop_description_path)
		translatable_description, _ = split_workshop_description(raw_description)
		description = apply_workshop_item_id(translatable_description, workshop_item_id)
		if description is None:
			print(f"{log_prefix}Workshop description could not be read; skipping workshop page translations.")
			return False

		translation_template = resolve_workshop_translation_template(
			workshop_template_path,
			main_workshop_template_path
		)

	# Load change notes (optional — missing, empty, or disabled is silently skipped).
	# Prefers docs/change_notes/<version>.bbcode, else the newest entry in the shared archive.
	change_notes = None
	if change_notes_path or change_notes_dir:
		entry = load_change_notes_source(change_notes_path, change_notes_dir, mod_version)
		if entry:
			change_notes = apply_workshop_item_id(entry, workshop_item_id)

	if description is None and change_notes is None:
		return False

	os.makedirs(workshop_translations_dir, exist_ok=True)

	workshop_cache = cache_bucket.setdefault("workshop", {})
	# Cache raw translated title/description per language so template changes don't force retranslation.
	translation_cache = workshop_cache.setdefault("translations", {})
	description_changed = False
	translator_changed = workshop_cache.get("description_translator") != workshop_description_translator
	description_hash = None
	if description is not None:
		description_hash = hash_text(description)
		# Re-translate when source text or provider changes.
		description_changed = workshop_cache.get("description_hash") != description_hash or translator_changed

	change_notes_changed = False
	change_notes_hash = None
	change_notes_translator_changed = workshop_cache.get("change_notes_translator") != workshop_description_translator
	if change_notes is not None:
		change_notes_hash = hash_text(change_notes)
		change_notes_changed = workshop_cache.get("change_notes_hash") != change_notes_hash or change_notes_translator_changed

	title_translator_changed = workshop_cache.get("title_translator") != workshop_title_translator
	template_hash = hash_text(translation_template) if translation_template is not None else None
	template_changed = template_hash != workshop_cache.get("template_hash")

	description_success = True
	title_success = True
	change_notes_success = True
	cache_changed = False

	for folder_name, deepl_code in target_languages.items():
		if folder_name == source_language:
			continue

		translation_path = os.path.join(
			workshop_translations_dir,
			WORKSHOP_TRANSLATION_FILENAME.format(lang=folder_name)
		)
		file_changed = False
		cache_entry = translation_cache.setdefault(folder_name, {})
		cached_title = cache_entry.get("title")
		cached_description = cache_entry.get("description")

		if title:
			if cached_title is None or title_translator_changed:
				print(f"{log_prefix}Translating workshop title -> {folder_name} "
				      f"({provider_label(workshop_title_translator)})...")
				translated_title = dispatch_title_translation(
					workshop_title_translator,
					translator,
					title,
					folder_name,
					deepl_code,
					source_lang_deepl,
					gemini_title_system_prompt,
					gemini_additional_context
				)
				if translated_title is not None:
					cached_title = translated_title
					cache_entry["title"] = translated_title
					cache_changed = True
					file_changed = True
				else:
					title_success = False
			else:
				print(f"{log_prefix}Workshop title cached -> {folder_name}; skipping.")

		if description is not None:
			needs_description = description_changed or cached_description is None
			if needs_description:
				print(f"{log_prefix}Translating workshop description -> {folder_name} "
				      f"({provider_label(workshop_description_translator)})...")
				translated_description = dispatch_block_translation(
					workshop_description_translator,
					translator,
					description,
					folder_name,
					deepl_code,
					source_lang_deepl,
					gemini_description_system_prompt,
					gemini_additional_context
				)
				if translated_description is None:
					description_success = False
					continue
				cached_description = translated_description
				cache_entry["description"] = translated_description
				cache_changed = True
				file_changed = True
			else:
				print(f"{log_prefix}Workshop description unchanged -> {folder_name}; skipping.")

		if change_notes is not None:
			cached_change_notes = cache_entry.get("change_notes")
			needs_change_notes = change_notes_changed or cached_change_notes is None
			if needs_change_notes:
				print(f"{log_prefix}Translating change notes -> {folder_name} "
				      f"({provider_label(workshop_description_translator)})...")
				translated_change_notes = dispatch_block_translation(
					workshop_description_translator,
					translator,
					change_notes,
					folder_name,
					deepl_code,
					source_lang_deepl,
					gemini_description_system_prompt,
					gemini_additional_context
				)
				if translated_change_notes is not None:
					cached_change_notes = translated_change_notes
					cache_entry["change_notes"] = translated_change_notes
					cache_changed = True
				else:
					change_notes_success = False
			else:
				print(f"{log_prefix}Change notes unchanged -> {folder_name}; skipping.")

			if cached_change_notes is not None:
				change_notes_translation_path = os.path.join(
					workshop_translations_dir,
					CHANGE_NOTES_TRANSLATION_FILENAME.format(lang=folder_name)
				)
				with open(change_notes_translation_path, "w", encoding="utf-8") as f:
					f.write(cached_change_notes)

		if translate_pages and (file_changed or template_changed or not os.path.exists(translation_path)):
			if cached_title is None and cached_description is None:
				continue
			translated_language = LANGUAGE_DISPLAY_NAMES.get(folder_name, folder_name)
			original_language = LANGUAGE_DISPLAY_NAMES.get(source_language, source_language)
			output = render_workshop_translation_text(
				translation_template,
				cached_title,
				cached_description,
				title,
				description,
				translated_language,
				original_language
			)
			with open(translation_path, "w", encoding="utf-8") as f:
				f.write(output)

	if description is not None and description_changed and description_success:
		workshop_cache["description_hash"] = description_hash
		workshop_cache["description_translator"] = workshop_description_translator
		cache_changed = True

	if change_notes is not None and change_notes_changed and change_notes_success:
		workshop_cache["change_notes_hash"] = change_notes_hash
		workshop_cache["change_notes_translator"] = workshop_description_translator
		cache_changed = True

	if title_success and workshop_cache.get("title_translator") != workshop_title_translator:
		workshop_cache["title_translator"] = workshop_title_translator
		cache_changed = True

	if workshop_cache.get("template_hash") != template_hash:
		workshop_cache["template_hash"] = template_hash
		cache_changed = True

	return cache_changed

def walk_localization_files(target, source_language):
	"""Yield (loc_base_path, source_filepath) for every source .yml under a target's loc roots."""
	for loc_base_path in target["loc_base_paths"]:
		source_dir = os.path.join(loc_base_path, source_language)
		if not os.path.isdir(source_dir):
			continue
		for root, _, files in os.walk(source_dir):
			for file in sorted(files):
				if file.endswith(".yml"):
					yield loc_base_path, os.path.join(root, file)

def translate_target_localization(
	target,
	translator,
	source_language,
	source_lang_id,
	source_lang_deepl,
	target_languages,
	localization_translator,
	gemini_localization_system_prompt,
	gemini_additional_context,
	file_hashes
):
	"""Translate every localization file for one target (main mod or a submod).

	Returns True when the hash cache changed. For the local backend this runs twice: a
	collect pass that records every string needing translation (so they can be batched),
	then the real pass that writes files using the batched results.
	"""
	log_prefix = target["log_prefix"]
	files = list(walk_localization_files(target, source_language))
	if not files:
		roots = ", ".join(target["loc_base_paths"]) or "(none)"
		print(f"{log_prefix}No '{source_language}' localization found under: {roots}; skipping.")
		if file_hashes:
			file_hashes.clear()
			return True
		return False

	# Pre-read each file once and work out which keys changed since the last run.
	parsed_files = []
	processed_files = set()
	hashes_modified = False
	for loc_base_path, source_filepath in files:
		with open(source_filepath, 'r', encoding='utf-8-sig') as f:
			source_lines = f.readlines()

		source_entries = parse_source_entries(source_lines)
		source_hashes = {entry["key"]: hash_text(entry["value"]) for entry in source_entries}

		# Key the cache on the mod root so files with the same name under different
		# content roots (in_game/ vs main_menu/) cannot collide.
		source_rel_path = os.path.relpath(source_filepath, target["mod_root"]).replace("\\", "/")
		processed_files.add(source_rel_path)

		prev_hashes = file_hashes.get(source_rel_path, {})
		changed_keys = {
			key for key, current_hash in source_hashes.items()
			if prev_hashes.get(key) != current_hash
		}

		parsed_files.append({
			"loc_base_path": loc_base_path,
			"source_filepath": source_filepath,
			"source_lines": source_lines,
			"source_entries": source_entries,
			"source_hashes": source_hashes,
			"source_rel_path": source_rel_path,
			"prev_hashes": prev_hashes,
			"changed_keys": changed_keys,
		})

	def run_pass():
		for info in parsed_files:
			for folder_name, deepl_code in target_languages.items():
				process_file(
					translator,
					info["source_lines"],
					info["source_entries"],
					info["source_filepath"],
					info["loc_base_path"],
					folder_name,
					deepl_code,
					source_lang_id,
					source_lang_deepl,
					info["changed_keys"],
					localization_translator,
					gemini_localization_system_prompt,
					gemini_additional_context,
					log_prefix
				)

	if BATCH.enabled:
		BATCH.collecting = True
		try:
			run_pass()
		finally:
			BATCH.collecting = False
		total = sum(len(v) for v in BATCH.pending.values())
		if total:
			print(f"{log_prefix}Collected {total} strings to translate across "
			      f"{len(BATCH.pending)} language(s).")
			BATCH.flush(gemini_localization_system_prompt, gemini_additional_context, log_prefix)
		else:
			print(f"{log_prefix}Nothing to translate; all localization is up to date.")

	run_pass()

	for info in parsed_files:
		if info["prev_hashes"] != info["source_hashes"]:
			file_hashes[info["source_rel_path"]] = info["source_hashes"]
			hashes_modified = True

	# Drop cache entries for source files that no longer exist.
	for rel_path in list(file_hashes.keys()):
		if rel_path not in processed_files:
			del file_hashes[rel_path]
			hashes_modified = True

	return hashes_modified

def main():
	"""Script entry point."""
	args = parse_args()

	(
		source_language,
		translate_workshop,
		translate_submods_by_default,
		translate_change_notes_by_default,
		localization_translator,
		gemini_localization_system_prompt,
		workshop_description_translator,
		gemini_description_system_prompt,
		workshop_title_translator,
		gemini_title_system_prompt,
		gemini_additional_context,
		workshop_item_id
	) = load_config(CONFIG_PATH)
	if not source_language:
		return

	source_lang_id = LANGUAGE_CONFIG[source_language]["loc_id"]
	source_lang_deepl = LANGUAGE_CONFIG[source_language]["deepl"]

	translate_mod, translate_wp, include_submods, translate_cn = resolve_translate_targets(
		args, translate_workshop, translate_submods_by_default, translate_change_notes_by_default
	)

	if not translate_mod and not translate_wp and not include_submods and not translate_cn:
		print(
			"No translation targets selected. "
			"Enable defaults in config.toml or pass -m/-wp/-s/-cn."
		)
		return

	# Only demand a DeepL key/package when a selected job actually uses DeepL.
	selected_translators = set()
	if translate_mod or include_submods:
		selected_translators.add(localization_translator)
	if translate_wp:
		selected_translators.update({workshop_title_translator, workshop_description_translator})
	if translate_cn:
		selected_translators.add(workshop_description_translator)
	if not require_deepl(selected_translators):
		return

	translator = get_translator() if "deepl" in selected_translators else None

	target_languages = resolve_target_languages(args.languages, source_language)
	if target_languages is None:
		return

	BATCH.enabled = localization_translator == LOCAL_TRANSLATOR
	if BATCH.enabled:
		print(f"Local translator: {LOCAL_SETTINGS['model']} at {LOCAL_SETTINGS['api_base']} "
		      f"(batch {LOCAL_SETTINGS['batch_size']}, concurrency {LOCAL_SETTINGS['concurrency']})")
	print(f"Target languages: {', '.join(sorted(target_languages))}")

	# Load existing hash cache to identify changed keys.
	hash_data = load_hashes(HASHES_PATH)
	hashes_modified = False

	if translate_wp and (workshop_item_id is None or workshop_item_id <= 0):
		print("Error: workshop_upload_item_id must be a positive integer in config.toml for workshop page translation.")
		return

	targets = build_translation_targets(include_submods)
	if include_submods:
		active_submods = {target["cache_key"] for target in targets if target["cache_key"] != "main"}
		submods_cache = hash_data.get("submods")
		if isinstance(submods_cache, dict):
			for cache_key in list(submods_cache.keys()):
				if cache_key not in active_submods:
					del submods_cache[cache_key]
					hashes_modified = True

	for target in targets:
		cache_bucket = get_cache_bucket(hash_data, target["cache_key"])
		file_hashes = cache_bucket["files"]

		if translate_mod:
			hashes_modified = translate_target_localization(
				target,
				translator,
				source_language,
				source_lang_id,
				source_lang_deepl,
				target_languages,
				localization_translator,
				gemini_localization_system_prompt,
				gemini_additional_context,
				file_hashes
			) or hashes_modified

		if translate_wp or translate_cn:
			hashes_modified = translate_workshop_assets(
				translator,
				source_language,
				source_lang_deepl,
				cache_bucket,
				workshop_description_translator,
				gemini_description_system_prompt,
				workshop_title_translator,
				gemini_title_system_prompt,
				gemini_additional_context,
				workshop_item_id,
				target["metadata_path"],
				target["workshop_description_path"],
				target["workshop_translations_dir"],
				target["workshop_template_path"],
				WORKSHOP_TRANSLATION_TEMPLATE_PATH,
				target["change_notes_path"] if translate_cn else None,
				target["change_notes_dir"] if translate_cn else None,
				load_metadata_version(target["metadata_path"]),
				target_languages,
				target["log_prefix"],
				translate_pages=translate_wp
			) or hashes_modified

	# Write cache only if something changed.
	if hashes_modified:
		save_hashes(HASHES_PATH, hash_data)

	print("Translation complete!")

if __name__ == "__main__":
	main()
