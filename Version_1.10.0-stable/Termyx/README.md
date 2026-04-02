# Termyx - Multi-Function CLI App

The app is currently on Version 1.10.0.

If you like what you see, consider joining the Discord Server at this link: https://discord.gg/GxPxfjGAef

**Termyx** is a lightweight, all-in-one command-line interface (CLI) application designed for quick, practical tasks directly from your terminal. Built with Python, Termyx offers a suite of tools for everyday productivity and learning exercises, all wrapped in a fun, retro-inspired interface.

## What's New in 1.10.0

- **Theme selection** - Choose from `default`, `ocean`, `ember`, `neon`, or `monochrome`, and save your preferred theme in `config.json`.
- **Release update check** - Termyx can notify you on startup when a newer GitHub release is available.
- **Rewritten calculator** - The calculator now supports full one-line expressions with brackets, functions, and constants.
- **Optional system monitor dependency** - `psutil` is no longer required to run the app itself. If it is not installed, only the System Monitor tool is hidden or disabled.
- **Improved startup flow** - Help and changelog screens display more clearly, and startup messaging has been cleaned up.
- **Encoding and text cleanup** - Source files and release text have been cleaned up for better consistency and compatibility.

## Features
- **Stopwatch** - Track elapsed time with start, stop, reset, and lap commands.
- **Timer** - Run a countdown timer in minutes or use interval mode with a custom start, end, step, and delay.
- **Calculator** - Evaluate full expressions such as `7 + 3 * 2`, `sqrt(144) + abs(-5)`, `round(pi, 2)`, or `sin(pi / 2)`.
- **Tally Counter** - Keep a running count by pressing Enter.
- **System Monitor** - View CPU, RAM, disk usage, battery information, and the current time in real time.
- **Random Number Generator** - Generate a random whole number between two chosen limits, including negative numbers.
- **Dice Roller** - Roll one or more dice with supported die types and animated output.
- **Unit Converter** - Convert between units of length, mass, and temperature.
- **Pomodoro Timer** - Run customizable work and break sessions based on the Pomodoro Technique.
- **Coin Flipper** - Flip a virtual coin with a simple spinner animation.
- **Theme Selection** - Personalize Termyx with multiple built-in colour themes.
- **Desktop shortcut setup** - Use the included Windows scripts to launch Termyx or create a desktop shortcut.
- **Interactive CLI flow** - Friendly prompts, validation, and tailored rerun prompts across tools.

## Calculator Functions

The `1.10.0` calculator supports:

- Operators: `+`, `-`, `*`, `/`, `**`, `//`, `%`
- Functions: `abs()`, `round()`, `sqrt()`, `log()`, `ln()`, `sin()`, `cos()`, `tan()`
- Constants: `pi`, `e`
- Grouping with brackets: `( )`

## Themes

Termyx includes five built-in themes:

- `default` - The classic Termyx experience. Warm and familiar.
- `ocean` - Cool blues and greens. Easy on the eyes.
- `ember` - Reds and warm tones. Bold and intense.
- `neon` - Bright magentas and cyans. High contrast and vibrant.
- `monochrome` - No colour distractions. Clean and minimal.

Your selected theme is stored in `Termyx/config.json` after you choose one in the app.


## Why Termyx?
Termyx is a good fit for learners, coders, and anyone who wants quick CLI utilities without leaving the terminal. Its modular structure also makes it easy to extend or customize.

## Prerequisites

To run Termyx, you will need:

- **Python 3.8+** - Download it from [python.org](https://www.python.org/downloads/).
- **A terminal or command-line interface** - Command Prompt, PowerShell, Windows Terminal, or another terminal that can run Python scripts.
- **`psutil` (optional)** - Only needed for the System Monitor tool.

Install `psutil` if you want System Monitor support:

```bash
pip install psutil
```

> **Note:** Termyx has been developed and tested primarily on **Windows 10+**. It should also work on macOS and Linux, but those platforms have not been tested as extensively.
> **Note:** If `psutil` is not installed, the rest of the app still works normally.

## File Structure

As of version `1.10.0`, Termyx uses the following layout:

```text
Version_1.10.0-stable/
|-- setup.ps1
|-- shortcut.bat
|-- termyx.bat
|-- termyx.ico
|-- termyx.sh
`-- Termyx/
    |-- README.md
    |-- changelog.md
    |-- config.json
    |-- main.py
    `-- Tools/
        |-- __init__.py
        |-- calculator.py
        |-- coin_flip.py
        |-- colours.py
        |-- dice.py
        |-- pom_tmr.py
        |-- rng.py
        |-- stopwatch.py
        |-- system_monitor.py
        |-- tally.py
        |-- timer.py
        |-- unit_conv.py
        `-- updater.py
```

Notes:

- `main.py` is the app entry point.
- Each tool lives in its own module inside `Tools/`.
- `config.json` is created or updated when a theme is saved.
- `termyx.bat` and `termyx.sh` are launcher scripts.
- `setup.ps1` and `shortcut.bat` support Windows setup and shortcut creation.

## How to Download

1. Go to the **Termyx releases page**.
2. Download the latest `Version_1.10.0-stable.zip` release.
3. Extract the archive to a location of your choice.
4. Optionally install `psutil` if you want the System Monitor tool:

```bash
pip install psutil
```

5. Launch the app using one of the following methods:

- **Windows** - Double-click `termyx.bat`
- **Windows shortcut setup** - Run `shortcut.bat` to create a desktop shortcut
- **macOS / Linux** - Run `./termyx.sh` from your terminal
- **Any platform** - Open the `Termyx/` folder and run `python main.py`

If `termyx.sh` is not executable yet, run:

```bash
chmod +x termyx.sh
```

## Additional Notes

- Termyx runs entirely in the terminal.
- The terminal tab title is set to `Termyx` on startup.
- On startup, the app can show update availability based on the latest GitHub release.
- If you encounter bugs or issues, please open an Issue on the repository or post in the Discord server.
- Always download the latest release to get the newest features and fixes.

## Versioning

Termyx uses semantic-style versioning:

`MAJOR.MINOR.PATCH`

Example:
`1.10.0`

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
