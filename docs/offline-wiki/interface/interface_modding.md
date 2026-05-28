# Interface modding guide

**Source:** https://eu5.paradoxwikis.com/Interface_modding_guide

---


## Basics

The interface in EU5 is highly modable, the vanilla files can be quite tricky to understand though.

It is highly recommended to run the game in debug mode (add -debug_mode) to your EU5 steam starting options. With debug mode the changes you are making in the files will be visible immediately and you don’t have to restart the game every time.

When opening the debug console you want to extensively use the **UI Bounds** (under 2D Tools). These option makes the gui visible and connects it the files. If you have over an UI element you will see that a black box opens and right on the top it says where this particular UI element can be found in the files. Often times you will have to cycle through some layers to get what you are interested in. Use Alt + LeftMouseButton to cycle through the GUI widgets. In theory you can directly open the file by pressing Alt+ RightMouseButton, but by default that will open the file in the Windows Notepad. You can choose which editor to use when opening files by setting the path in **Settings → Game → System → Editor** (double every backslash: for instance write `C:\\Program Files\\Notepad++\\notepad++.exe` instead of `C:\Program Files\Notepad++\notepad++.exe`).

You also need to know that gui files both can be found in the **in_game/gui** and **main_menu/gui** folders. You might have to search both folders in order to find what you are looking for. Unfortunately as of now the UI Bounds option won’t show you directly whether you need to search in **in_game/gui** or **main_menu/gui**.

## Understanding the files and their structure

GUI files in EU5 are organized in a very modular way, that means that you will most of the time not find everything you need for something in the interface to change in one file only, but in many files.

The reason for this is that EU5 uses types and templates that are set up in one file and referenced in other files.

That has the advantage that you can reuse templates and types over and over again, but it also makes it more difficult to get an overview over things when starting out.

### Templates

Templates are containers for properties. So **"using = template_name"** simply adds all properties (for example size) of widgets and containers, that are in the template block, to the current widget/container the template is referenced by. You can use those if you have a repeatable UI elements that always have the same structure.

```
template new_template_name {
    container = {   } # this is a container  
   size = { 100 100 } # this is a property
}
```

### Types

Types are widgets/containers in itself that allow reuse and overwriting properties in it. You may want to use those when you want to set up something you want to reuse later.

```
types my_types_general_naming {
    type example_base_type = widget { # this is an example type of a widget
        # Here you can define a set of overwritable properties, widgets or containers
        block "test_block" {
            size = { 100 100 }
        }
    }
}
```

Types can be referenced anywhere. This might look like this:

```
widget = {
   example_base_type = {} # this is the type we added above
}
```

### Windows

Windows are the top entities in the UI. Everything that can be seen in the game is inside some window. That means if you want to set up a completely new entity of some interface, you will always have to create a new window.

### Widgets

Widgets are essentially smaller windows of UI elements grouped together. They are similar to windows in that, that all of the things that you want to interact with need to be in a widget.

### Updating of GUI files in game though calculation

You may encounter instances where you have added scripted variables that are displayed on some window you have added and you might find that the display of those variables are not auto updated in some cases.

One of the cases where a scripted variable is not updated when a calculation changes that variable. The GUI will, in some cases, only update when the calculation of the variable is done by an event that is clicked by the player. Doing the calculation via an on action or an invisible event will give the correct results of the calculation, but the interface might not update.

This seems to only be the case for displayed variables by text as progressbars for instance update on the monthly tick.

## Designing your first custom window

In this section concrete examples will be provided to add some new UI elements from scratch. Beware, a lot of code. The examples are all taken from the mod The Idea Variation 2 and modified to fit the guide.

### How to make a new window

First create a new .gui file in your **modfolder/in_game/gui** folder. You can name it whatever you want, but for this example we will call it “mymod_interface.gui”.

Then you need to add a window to this file. The name of the window is also up to you, but for this example we will call it “mymod_window”.

The most basic window will look like this in the “mymod_interface.gui” file:

```
window = {
    name = "mymod_window" # this is the name we chose above
	parentanchor = center # this determines where the window appears on your screen, in this case in the middle
	size = { 100% 100% } # this determines the size of your window (in this case full screen)
	alwaystransparent = yes # this makes it so that the window does not block mouse clicks on UI below it
}
```

### Opening and closing your window

There are two ways you can go about opening and closing your window, through a variable bound to its visibility or through console commands.

While both ways will work the same, the variable toggle is a bit more idiomatic and thus recommended.

#### 1. Using a variable toggle

Make a new folder in your **modfolder/in_game/gui** that is called “**scripted_widgets**”.  This folder is not in the vanilla files but without it your window will not appear (unless using the console command way).

There you want to create a new .txt file (make sure its encoded in UTF-8-BOM) and add your windows like this:

```
gui/mymod_interface.gui = mymod_window
```

This adds the window: “**mymod_window**”

“**mymod_interface.gui**” is the file name of the gui file the window is in.

“**gui**/” is the path from your in_game folder.

Then you will need to bind the visible property of your window to a variable like this:

```
window = {
    name = "mymod_window" # This is the name we chose above
	parentanchor = center # this determines where the window appears on your screen, in this case in the middle
	size = { 100% 100% } # this determines the size of your window (in this case full screen)
	alwaystransparent = yes # this makes it so that the window does not block mouse clicks on UI below it
	visible = "[GetVariableSystem.Exists('mymod_window_open')]" # If the variable “mymod_window_open” exists, the window will be visible, you can name the variable whatever you want.
}
```

This will then open/close your window:

```
onclick = "[GetVariableSystem.Toggle('mymod_window_open')]"
```

#### 2. Using console commands

This will open your window:

```
onclick = "[ExecuteConsoleCommand('GUI.CreateWidget gui/mymod_interface.gui mymod_window')]"
```

This will close your window:

```
onclick = "[ExecuteConsoleCommand('GUI.ClearWidgets mymod_window')]"
```

If you have several scripted windows open you can also use this to close them all:

```
onclick = "[ExecuteConsoleCommand('gui.clearwidgets')]"
```

### Accessing the new window by using a button

It makes sense to create ourselves a type for our new button as this will make mod compatibility easier down the line, as most mods might want to edit the main interface files.

Lets add a type for a button that will open the idea window:

```
types iv2_main_idea_button { 
	type button_panel_tab_ideas = button_panel_tab_alt {  # “button_panel_tab_ideas” is the name of the type; “button_panel_tab_alt” is the type of the button
						
		tooltipwidget = { # this is the tooltip that is shown when hovering over the button
			using = iv2_idea_tab_tt
		}
				
        onclick = "[GetVariableSystem.Toggle('mymod_window_open')]" # Or via "[ExecuteConsoleCommand('GUI.CreateWidget gui/mymod_interface.gui mymod_window')]" if you want to use the console command way.
					
		input_action = "top_left_9" # hotkey stuff
		use_global_input_instance = yes # hotkey stuff

		using = layoutpolicy_expanding 

		icon = {	 # this is the icon that is shown on the button			
			position = { 0 -1 }
			size = { 35 35 }
			parentanchor = center
			texture = "gfx/interface/icons/icon_idea_menu_2.dds"
			texture_density = 2	
			}
		}
}
```

If we add this type like this, we only need this to add to the vanilla file (in this case the left_panel.gui, where the main menu interfaces is at:

```
button_panel_tab_ideas = {}
```

That is a lot easier to keep updated with changing vanilla files and to keep compatible with other mods.

### Add a close button to your new window

A closing button would look like this:

```
widget = {
	parentanchor = right
	position = { 0 130 } 
	size = { 40 40 }

	ui_direction_button_holder_right = {}

	button_close_alt = {
		blockoverride "close_onclick"
		{
	        onclick = "[GetVariableSystem.Toggle('mymod_window_open')]" # Or via "[ExecuteConsoleCommand('GUI.ClearWidgets mymod_window')]" if you want to use the console command way.
		}
	}
}
```

### Changing how our window will look in game

There are many ways to set up your window. The following code is merely one way to do the background art and a very basic example. The things you can do are almost limitless. Copy this part to the top of your window to see for yourself. Comment in some of the things that were commented out to see what they do and how they change the look of your window.

```
vbox = {
	using = lateralview_full_margins # this is a window template 
	
	widget = {
		using = layoutpolicy_expanding
		alwaystransparent = no
		allow_outside = yes
	
		using = bg_lateralview
				
		blockoverride "inside_color" {
			modify_texture = {
				#using = color_dark_purple_texture
				#blend_mode = multiply
			}
		}

		vbox = {
			block "panel_header" {}

			hbox = {
				using = layoutpolicy_expanding

				widget = {
					using = layoutpolicy_expanding
					block "panel_content" {}
					window_bottom_paper_template = {}
				}

				block "panel_content_side"
				{
					icon = {
						layoutpolicy_vertical = expanding
						size = { 30 -1 }

						using = color_dark_brown_texture
						#using = overlay_window
						#using = overlay_leather
					}
				}
			}
		}
				
		#lateralview_topbuttons = {} # this is a type
		#window_bottom_paper_template = {} this is a type
	}
}
```

## Adding advanced UI elements

This section will teach you how to add some more advanced UI elements.

### Adding a character portrait to our new window

You can add a character portrait to your new window and display a certain character on your interface like this:

```
widget = {					
	size = { 160 160 }
	position = { 15 235 }
					
        character_frame_small = { # the type of the frame, you can search the game files for other options
		parentanchor = left
		blockoverride "portrait_datacontext" {			
			datacontext = "[Country.MakeScope.GetVariable('Iv2_researcher_adm').GetCharacter]" # this is the most important thing. This datacontext shows the character in your country with the Variable “'Iv2_researcher_adm'” You will need to set the variable by some other means, like an event, a character interaction or some generic action.			
		}
		block "character_frame_size" {
			size = { 160 160 } #  size of the frame
		}
		blockoverride "character_frame_texture" {
			texture = "gfx/interface/component_decoration/character_frames/character_non_stretchable_frame_2.dds"
		}
		blockoverride "character_portrait_visible" {
			visible = yes
		}
		blockoverride "character_portrait_ani_visible" {
			visible = no
		}
	}
}
```

### Adding a progress bar

You can add a progress bar of a scripted variable you added, if you want to add a new resource of some sort to the game for instance. The code looks like this:

```
widget = {					
	size = { 400 20 } # size of your widget
	position = { 40 405 } # position of this widget in your window
								
	icon = { #  this is the frame of the progress bar in order for it to look nice
		name = "frame"					
		size = { 430 20 }	
		texture = "gfx/interface/progressbar_frame_iv2_4.dds"
		spriteType = Corneredstretched
		parentanchor = center
		position = { 7 0 }
								
		using = button_panel_tab_icon_effect
								
		glow = {
			name = "drop_shadow"
			glow_radius = 3
			color = {0.0 0.0 0.0 1.0}
			alpha = 0.8
			}	 
		}
								
		hbox = {
		layoutpolicy_horizontal = expanding
		margin = { 2 0 }

		progressbar = {
		size = { 410 14 } # adjust this size to the size of your frame for it to look nice
		using = progress_bar_blue_grey_alt #  this is a type
		min = 0 # this is the min point of your bar, can also be a scripted value
        max = "[FixedPointToFloat(Country.MakeScope.Var('iv2_var_innovation_points_limit_adm').GetValue)]" # see this example how to set the max point of your progress bar via a scripted value
	    value = "[FixedPointToFloat(Country.MakeScope.Var('iv2_var_innovation_points_adm').GetValue)]" # this value determines what is shown on the progress bar.
		noprogresstexture = "gfx/interface/progressbars/progress_gray_bg.dds"
		block "progress_setup" {}
										
		tooltipwidget = { # this is a tooltip shown when you hover over the bar
			using = iv_scrollbar_adm_tooltip_template
			}						
		}
	}	
}
```

### Add a button for a generic action

Generic actions are used for almost every button/interaction that has an immediate effect in the game, e.g. hiring a general or a courtier and so on.

Adding a button for new custom added generic actions looks like this:

```
card_header_action_button_04 = {
	size = { 80 40 }
	position = { 180 300 }
						
	actor = "[Player]" # this references who is clicking the button; Player in this case is the country
	parameter = {
		parameter_name = "target" #this references who gets the effect when the button is pressed
		parameter_value = "[Country]"
	}
						
	left_click_and_hold_action = { action_name = "iv2_ga_hire_researchers_adm" } # this references your generic action
						
	tooltipwidget = { # this is a tooltip again
	using = iv2_tooltip_template_res_adm
	blockoverride "tooltip_content" {
		using = action_tooltip_inner_content
		}
	}
						
	icon = {
		size = { 36 36 }
		parentanchor = center
		texture = "gfx/interface/icon_hire_adm.dds"
		texture_density = 2
		using = button_panel_tab_icon_effect
		glow = {
			name = "drop_shadow"
			glow_radius = 3
			color = {0.0 0.0 0.0 1.0}
			alpha = 0.8
		}					
	}
}
```

### Using buttons to nicely group things together

Buttons can also be used to efficiently display information that is ultimately not clickable. Like this you have nice area to hover over to display a tooltip.

This button for instance displays an icon and a text (in this case a dynamic variable).

```
button_default = {
	size = { 80 40 }
	position = { 1300 280 }
	
	tooltipwidget = {
		using = iv_scrollbar_army_tooltip_template
	}
	
	hbox = {
		position = { -20 1 }
		margin = { 20 0 }
		
		icon = {
			size = { 28 28 }
			texture = "gfx/interface/icon_innovation_points_army.dds"
			texture_density = 2

			using = button_panel_tab_icon_effect

			glow = {
				name = "drop_shadow"
				glow_radius = 3
				color = {0.0 0.0 0.0 1.0}
				alpha = 0.8
			}
		}
	}
	hbox = {
		position = { 15 0 }
		text_single = {
			name = "iv2_text"
			text = "IV_IDEAGROUP_CURRENT_POINTS_TEXT_ARMY"
		}
	}					
}
```

## Setting up Tooltip Widgets

Setting up tooltip widgets can be quite tricky, but basically every information you want can be displayed with the right hovarable tooltip.

### Referencing tooltips in the files

Tooltips can be placed virtually anywhere. They can be on an icon, on a button, on some text, on a scrollbar. You might have seen some examples already in the examples provided above.

Lets take a look at their basic structure in the files:

First example:

```
tooltipwidget = {
	using = iv_scrollbar_navy_tooltip_template
}
```

Second example:

```
tooltipwidget = {
	using = iv2_tooltip_template_res_navy # this is a tooltip template
	blockoverride "tooltip_content" { # this changes the basic tooltip template in this special case
		using = action_tooltip_inner_content
	}
}
```

Templates are excessively used with tooltip widgets in vanilla EU5, which is why it can be quite tricky to track them down to the source. The second example shows that we can change our basic template within a tooltip widget without creating a new template.

This is how the templates of the examples above look:

```
template iv2_tooltip_template_res_navy {
	ContextualTooltipType = {
		blockoverride "title_icon" {
			icon = {
				using = tooltip_title_icon_size
				texture = "gfx/interface/icon_hire_navy.dds"

				glow = {
					name = "drop_shadow"
					glow_radius = 3
					color = {0.0 0.0 0.0 1.0}
					alpha = 0.3
				}
			}
		}

		blockoverride "title_text" {
			text = "iv2_ga_hire_researchers_navy"
		}

		blockoverride "concept_link" {
			text = "[iv2_researcher|e]"
		}
	}
}
```

With this template you can see that the vanilla “ContextualTooltipType” was used and changed for our special tooltip to work to our liking. Sometimes it matters which vanilla tooltip type you choose as not every information can be referenced everywhere. Depending on what you choose you might encounter things not working as you intended.

## References


