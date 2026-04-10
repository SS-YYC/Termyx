# Version 1.11.1
## is here with the following

## New Features

- Began Phase 1 of a 2-part download overhaul, with packaged downloads and startup improvements now in place ahead of a future installer.
- Downloaded Windows builds can now be launched directly from the packaged `Termyx.exe`, with shortcut creation aimed at the packaged app instead of the source files.

## App Improvements

- Standardized all general error messages to `Invalid entry.`.
- The opening banner's version and tagline text are now dynamic.
- The app will no longer notify you if you are on the latest version, but will still notify you if a new version is avaliable.
- The calculator history limit has been increased to 10 entries.
- The updater can now distinguish internet issues from other check failures and shows a clearer unavailable-status message when needed.

## Scripting Improvements

- Changed the directory code to now take aliases from a dictionary.
- The terminal tab will now display `Termyx - RNG` instead of `Termyx - Random Number Generator` to better fit smaller displays.
- The coin flipper's spin time has been decreased to 1 second instead of 2.
- Various minor scripting improvements.

## Bug Fixes

- The Elimination Wheel will no longer incorrectly loop and erase all values after each spin. The `Spin again (Y/n)?` message will show only on the Random Wheel.
- Fixed incorrectly decrementing times in the Pomodoro Timer by adjusting code positioning.
- Incorrect punctuation and grammar across the app has been fixed.
