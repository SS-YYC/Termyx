# Version 1.11.0 - Flow State
## is here with the following

## New Features

- Added a Wheel Spinner tool with random-pick and elimination modes for custom option lists.
- Added calculator history so the last 5 answers are saved in config.json and remembered between sessions.
- Added a dedicated `history (h)` command in the Calculator to view saved answers on demand.

## App Improvements

- Clarified prompts and status messages across the app for cleaner, more consistent wording.
- Improved repeat-prompt defaults and command exit hints so tool flow feels more consistent.
- Standardized `quit (q)` as the visible exit keybind across the app.
- Refreshed the splash screen with a cleaner welcome flow at startup.
- Updated the startup ASCII art for the new splash screen.
- Updated the startup intro with a simpler welcome line and a local date-and-time display.
- Added a saved 12-hour or 24-hour time format setting for the splash screen and System Monitor.
- Removed unnecessary repeat prompts from quick-use tools so they stay open until you choose to quit.
- Improved helplinks screen.

## Scripting Improvements

- Added clean `EOFError` handling across the app so tools return more gracefully when input is closed unexpectedly.
- Standardized prompt spacing so prompts now consistently show the message, a blank line, and then `>`.
- Better System Monitor references when it's unavailable.
- Various minor scripting improvements for easier future development.

## Bug Fixes

- Fixed `(Y/n)` prompts so pressing Enter now consistently uses the default `Yes` behavior.
- Fixed awkward leftover wording in a few prompts and status messages.
