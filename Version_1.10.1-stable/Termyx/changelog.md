# Version 1.10.1
## is here with the following

## New Features

- Three new themes have been added:
    - Forest - Deep greens and earthy tones. Calm and grounded.
    - Amber - Warm ambers and whites. Retro and nostalgic.
    - Dracula - Purples and greens. Dark and mysterious.    
## App Improvements

- Pomodoro defaults can now be changed and saved from the settings menu.
- User settings are now saved in a per-user config location, so they persist across app updates.
- Theme and Pomodoro settings now survive when users download and switch to a newer Termyx version.
- The terminal tab name now updates to show the active tool while you use it.
- A new settings menu groups theme selection and Pomodoro defaults in one place.

## Scripting Improvements

- The update checker now compares version numbers safely, which avoids false update notices on newer builds.
- Update notices now show the latest available version directly in the startup message.
- Repeat prompts across the tools now use a consistent `(Y/n)` format.

## Bug Fixes

- Theme changes no longer overwrite other saved settings such as Pomodoro defaults.
