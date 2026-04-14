# Version 1.12.0 - Unlocked
## is here with the following

## New Features

- A Password Generator has been added for creating secure random passwords with customizable options.
- Configurable directory order has been added so users can reorder or hide tools from the directory.
- A config viewer has been added inside Settings to show all saved values in one place.
- A config reset option has been added to restore the app back to defaults from within Settings.
- Config export and import support has been added for shareable `.json` presets.
- The ability to name stopwatch sessions has been added.
- Imperial units have been added to the Unit Converter alongside the existing metric options.

## App Improvements

- Added a Startup Behaviour setting that can skip the splash screen and go straight to the directory with a simple welcome message.
- Many new aliases are available during tool selection to better account for misinterpretations by users.

## Scripting Improvements

- The calculator's error handling has been improved to better handle specific and rare computer errors.
- Unnecessary (and annoying) directory logic has been removed.
- Splash screen BTS improvements - no user facing changes, but some things have been shifted to avoid rare errors and miscompilation.
- `shortcut.bat` and `setup.ps1` have been deleted as they aren't needed anymore with the new installer and application startup procedures.

## Bug Fixes

- Outdated help info from Versions 1.10 and 1.11 have been added to the help menu.
- Calculator error handling has been improved to avoid false errors.
- Several strings have been made raw to avoid throwing `SyntaxWarning`s when running from the codebase.
- Broken directory aliases inherited from 1.11.2 have been fixed so shorthand tool commands resolve correctly again.
