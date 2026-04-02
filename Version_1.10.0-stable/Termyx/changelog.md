# Version 1.10.0 - Termyx your way
## is here with the following

## New Features

- Theme selection has been added. Select your preferred theme at the directory and it'll be saved for the future (this must be completed after every new Termyx release).
    - The following themes are available:
        - Default - The classic Termyx experience. Warm and familiar.
        - Ocean - Cool blues and greens. Easy on the eyes.
        - Ember - Reds and warm tones. Bold and intense.
        - Neon - Bright magentas and cyans. High contrast and vibrant.
        - Monochrome - No colour distractions. Clean and minimal.
- New colours have been added.
- The app will now notify you if there are any new releases available on startup.
- The calculator has been completely rewritten to support full expression input — type your entire calculation in one line (e.g. `7 + 3 * 2` or `sqrt(144) + abs(-5)`). Brackets are fully supported.
    - New operations added: `abs()`, `round()`, `sqrt()`, `log()`, `ln()`, `sin()`, `cos()`, `tan()`, `pi`, `e`
    - The previous step-by-step input method has been replaced.

## App Improvements

- The startup greeting now uses the standard primary colour for better visibility.
- `psutil` is now no longer a dependency to run the entire app.
    - All references to the system monitor will disappear if `psutil` isn't installed.
    - Run `pip install psutil` in your terminal to enable it.
    - If `psutil` isn't installed, installation instructions will be displayed upon startup.
- The terminal tab name will now change to Termyx upon startup. This will be expanded to individual tools soon.

## Scripting Improvements

- The startup changelog path now correctly prints the changelog before waiting for Enter.
- The startup help path now correctly prints the help text before waiting for Enter.
- Return-to-directory messaging is correctly shown as a separate prompt after startup help or changelog text.
- Directory changelog and help options print correctly with `input()` removed to avoid confusion with prompts.
- Redundant opening commands have been removed - these can still be accessed from the directory.

## Bug Fixes

- Fixed startup help and changelog screens being passed directly into `input()`, which could make their prompts less clear.
- The encoding of `main.py` has been changed from UTF-8 with BOM to UTF-8 to avoid unexpected `SyntaxError` warnings on older versions of Python.
- Remaining Python and Markdown source files have been standardized to UTF-8 without BOM for consistency and cleaner compatibility across tools and Python versions.
- Misplaced corrupted Mojibake across the app has been removed.
- Indentation, stripping and newline errors have been fixed in the dice roller.
- Fixed the Pomodoro summary showing the wrong number of short and long breaks after a completed session.
