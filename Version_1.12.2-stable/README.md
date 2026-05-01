# Termyx - Multi-Function CLI App

The app is currently on Version 1.12.2.

If you like what you see, consider joining the Discord Server at this link: https://discord.gg/GxPxfjGAef

**Termyx** is a lightweight, all-in-one command-line interface (CLI) application designed for quick, practical tasks directly from your terminal. Built with Python, Termyx offers a suite of tools for everyday productivity and learning exercises, all wrapped in a fun, retro-inspired interface.


## Features
- **Stopwatch** - Track elapsed time with start, stop, reset, and lap commands. Name your session before starting.
- **Timer** - Run a countdown timer in minutes or use interval mode with a custom start, end, step, and delay.
- **Calculator** - Evaluate full expressions such as `7 + 3 * 2`, `sqrt(144) + abs(-5)`, `round(pi, 2)`, or `sin(pi / 2)`, and review saved results with `history (h)`.
- **Tally Counter** - Keep a running count by pressing Enter.
- **System Monitor** - View CPU, RAM, disk usage, battery information, and the current time in real time.
- **Random Number Generator** - Generate a random whole number between two chosen limits, including negative numbers.
- **Dice Roller** - Roll one or more dice with supported die types and animated output.
- **Wheel Spinner** - Spin between custom options in random-pick or elimination mode.
- **Unit Converter** - Convert between metric and imperial units of length, mass, and temperature.
- **Pomodoro Timer** - Run customizable work and break sessions based on the Pomodoro Technique.
- **Coin Flipper** - Flip a virtual coin with a simple spinner animation.
- **Password Generator** - Create secure random passwords with configurable length and character options.
- **Theme Selection** - Personalize Termyx with multiple built-in colour themes.
- **Settings Menu** - Manage theme selection, Pomodoro defaults, time format, startup behaviour, directory layout, config viewing, config reset, and config import/export all in one place.
- **Desktop shortcut setup** - The Windows installer handles shortcut creation automatically.
- **Interactive CLI flow** - Friendly prompts, validation, visible `quit (q)` guidance, and smoother repeated use in quick tools.

## Calculator Functions

The `1.12.2` calculator supports:

- Operators: `+`, `-`, `*`, `/`, `**`, `//`, `%`
- Functions: `abs()`, `round()`, `sqrt()`, `log()`, `ln()`, `sin()`, `cos()`, `tan()`
- Constants: `pi`, `e`
- Grouping with brackets: `( )`
- History command: `history`, `hist`, `h`

## Settings

The Settings menu in `1.12.2` includes:

- Theme selection
- Saved Pomodoro defaults
- 12-hour or 24-hour time format
- Startup behaviour (show splash screen or skip to directory)
- Directory layout (reorder or hide tools from the directory)
- View saved config (see all saved values in one place)
- Reset config (restore all settings to defaults)
- Export config preset (save your settings to a shareable `.json` file)
- Import config preset (load settings from a `.json` preset file)

These settings are stored in the per-user config file and are remembered between releases.

## Themes

Termyx includes eight built-in themes:

- `default` - The classic Termyx experience. Warm and familiar.
- `ocean` - Cool blues and greens. Easy on the eyes.
- `ember` - Reds and warm tones. Bold and intense.
- `neon` - Bright magentas and cyans. High contrast and vibrant.
- `monochrome` - No colour distractions. Clean and minimal.
- `forest` - Deep greens and earthy tones. Calm and grounded.
- `amber` - Warm ambers and whites. Retro and nostalgic.
- `dracula` - Purples and greens. Dark and mysterious.

Your selected theme, saved Pomodoro defaults, calculator history, time format, startup behaviour, and directory preferences are stored in a per-user config file. On Windows, this is typically:

`C:\Users\<you>\AppData\Roaming\Termyx\config.json`


## Why Termyx?
Termyx is a good fit for learners, coders, and anyone who wants quick CLI utilities without leaving the terminal. Its modular structure also makes it easy to extend or customize.

## Prerequisites

For most users:

- **No separate Python installation is required** - the Windows installer is the default way to download and set up Termyx.

If you are running Termyx from source for development, you will need:

- **Python 3.8+** - Download it from [python.org](https://www.python.org/downloads/).
- **A terminal or command-line interface** - Command Prompt, PowerShell, Windows Terminal, or another terminal that can run Python scripts.
- **`psutil` (optional)** - Only needed for the System Monitor tool.

Install `psutil` if you want System Monitor support when running from source:

```bash
pip install psutil
```

> **Note:** Termyx has been developed and tested primarily on **Windows 10+**. It should also work on macOS and Linux, but those platforms have not been tested as extensively.
> **Note:** If `psutil` is not installed, the rest of the app still works normally when running from source.

## File Structure

As of version `1.12.2`, Termyx uses the following layout:

```text
Version_1.12.2-stable/
|-- termyx.ico
|-- README.md
|-- changelog.md
|-- main.py
|-- Termyx.spec
|-- dist/
`-- Tools/
    |-- __init__.py
    |-- calculator.py
    |-- coin_flip.py
    |-- colours.py
    |-- config_store.py
    |-- dice.py
    |-- password_gen.py
    |-- pom_tmr.py
    |-- rng.py
    |-- settings.py
    |-- stopwatch.py
    |-- system_monitor.py
    |-- tally.py
    |-- timer.py
    |-- unit_conv.py
    |-- updater.py
    `-- wheelspin.py
```

Notes:

- `main.py` is the app entry point.
- Each tool lives in its own module inside `Tools/`.
- `config_store.py` manages the per-user config path and migration from older in-folder settings.
- `settings.py` manages the settings menu, themes, Pomodoro defaults, time format, startup behaviour, directory layout, and config import/export.
- `dist\Termyx.exe` is the packaged Windows app built with PyInstaller.

## How to Download

1. Go to the **Termyx releases page**.
2. Download the latest Windows installer from the release.
3. Optionally install `psutil` for the best experience, especially if you want to use the System Monitor tool. In your terminal, run:

```bash
pip install psutil
```

4. Run the installer.
5. Follow the setup prompts.
6. Open the app from your Desktop folder after setup finishes.

If you are a developer and want to run Termyx from source instead:

1. Download or clone the project files.
2. Optionally install `psutil` if you want the System Monitor tool:

```bash
pip install psutil
```

3. Run:

```bash
python main.py
```

## How to Run the Installer

The Windows installer is the standard way to install Termyx.

1. Download the installer from the latest release.
2. Double-click the installer.
3. Follow the prompts shown on screen.
4. When setup finishes, look in your Desktop folder for the Termyx app or shortcut.

Notes:

- The exact installer filename may vary by release.
- If Windows shows a security prompt, confirm that you want to continue only if the file came from the official Termyx release.
- Running from source is mainly intended for development and testing.

## Additional Notes

- Termyx runs entirely in the terminal.
- The terminal tab title is set to `Termyx` in the directory and updates to match the active tool when launched.
- On startup, the app can show update availability based on the latest GitHub release and display the newest available version.
- Theme, time, calculator history, Pomodoro settings, startup behaviour, and directory preferences are remembered between releases through the per-user config file.
- Several quick-use tools stay open until you explicitly quit, instead of prompting after every action.
- If you encounter bugs or issues, please open an Issue on the repository or post in the Discord server.
- Always download the latest release to get the newest features and fixes.

## Versioning

Termyx uses semantic-style versioning:

`MAJOR.MINOR.PATCH`

Example:
`1.12.2`

- **MAJOR** - Larger structural changes or major new features
- **MINOR** - New tools, improvements, or visible feature upgrades
- **PATCH** - Bug fixes and smaller adjustments

## License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

This means you are free to:

- Use the software
- Modify the source code
- Distribute copies
- Distribute modified versions

Any redistributed or modified versions must also remain under GPL-3.0 and include the original license.

For full details, see the `LICENSE` file included in the repository or read the license here:
https://www.gnu.org/licenses/gpl-3.0.en.html