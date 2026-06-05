# Variable Audit — Engine False Positives

Variables flagged by the engine as "set but never used" that are working correctly
at runtime. Do not remove these writes.

---

## `unlocked_estate_privilege_magyar_supremacy`

**Engine message:** `Variable 'unlocked_estate_privilege_magyar_supremacy' is set but is never used`

**Status: False positive — safe to ignore.**

### Why it's flagged

The variable is set by the vanilla scripted effect `unlock_estate_privilege_effect`
via macro substitution:

```pdx
# in game/in_game/common/scripted_effects/country_effects.txt
unlock_estate_privilege_effect = {
    custom_description = {
        text = unlock_estate_privilege_effect
        value = estate_privilege:$type$
        set_variable = {
            name = unlocked_estate_privilege_$type$   # ← macro expansion
            value = yes
        }
    }
}
```

Called in `cc_game_start.txt` as:

```pdx
unlock_estate_privilege_effect = { type = magyar_supremacy }
```

Which expands at runtime to `set_variable { name = unlocked_estate_privilege_magyar_supremacy ... }`.

The variable is subsequently **read** by the corresponding `lock_estate_privilege_effect`
scripted effect through the same `$type$` macro, and by any estate privilege tooltip
or condition that checks for unlocked privileges.

The engine's static analysis cannot follow macro (`$parameter$`) substitution — it
sees only the literal string `unlocked_estate_privilege_$type$` in the source, not
the expanded form. It therefore cannot trace the read side, and flags the write as
orphaned.

### What to do

Nothing. This is standard Paradox estate privilege bookkeeping. Every estate privilege
defined in the game uses the same pattern and generates the same warning. The variable
is functional.

If the log noise is bothersome, there is no supported way to suppress individual
variable warnings in EU5 without removing the call — which would break the privilege
unlock display. Leave it as-is.
