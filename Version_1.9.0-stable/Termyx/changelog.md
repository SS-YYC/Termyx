# Version 1.9.0 - Rewired
## is here with the following updates:

## New Features

- A new `shortcut.bat` file has been added to create a desktop shortcut for Termyx.
- `setup.ps1` and `termyx.ico` have been added to support that shortcut flow on Windows.
- Stopwatch lap times have been added with the new `lap (l)` command.
- All recorded lap times are now displayed when the stopwatch is closed.
- Stopwatch commands now support shorthands: `start (s)` | `stop (st)` | `reset (r)` | `lap (l)` | `quit (q)`.
- `q` is now supported as a shorthand for `quit` in System Monitor.
- `q` is now supported as a shorthand for `quit` in Tally Counter.

## App Improvements

- Stopwatch times are now displayed in MM:SS format instead of raw seconds.
- In System Monitor, `q` replaces the previous `stop` command.
- The System Monitor refresh rate has been increased from 0.5 seconds to 0.25 seconds.
- In Tally Counter, `q` replaces the previous `stop` command.
- A time-of-day greeting is now shown on launch.
- The opening banner now includes the greeting directly.
- Intro lines across tools have been rewritten to feel more personal and tool-specific.
- Again prompts across tools have been updated to better match each tool.
- The main directory has been reformatted to separate commands from tools.
- `changelog (cl)` and `help (h)` can now be accessed directly from the central directory.
- When the changelog or help text is opened at startup, the app now waits for Enter before continuing to the directory.

## Scripting Improvements

- Unnecessary `ValueError` handling has been removed from the main directory loop.
- Command routing in `main.py` has been expanded to support the new central `changelog` and `help` commands.
- Minor flow and formatting improvements have been made across the app.

## Bug Fixes

- `os.system("")` has been restored in `main.py` to re-enable ANSI colour handling on Windows Command Prompt.
- Stopwatch reset output now stays consistent with the new MM:SS display format.
- Previous naming changes such as `System Monitor` and `Coin Flipper` remain consistent throughout the app.
