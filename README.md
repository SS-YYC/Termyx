# Termyx - Multi-Function CLI App

The app is currently on Version 1.9.0.

If you like what you see, consider joining the Discord Server at this link: https://discord.gg/GxPxfjGAef

**Termyx** is a lightweight, all-in-one command-line interface (CLI) application designed for quick, practical tasks directly from your terminal. Built with Python, Termyx offers a suite of tools for everyday productivity and learning exercises, all wrapped in a fun, retro-inspired interface.

## Features
- **Stopwatch** - Track elapsed time with start, stop, reset, and lap commands.
- **Timer** - Set a countdown timer in minutes, or use interval mode to count down from a starting number to an end number with a custom step and delay.
- **Calculator** - Perform arithmetic operations (`+`, `-`, `*`, `/`, `**`, `//`, `sqrt`, `%`) including exponents, floor division, square root, and percentage.
- **Tally Counter** - Keep track of counts by pressing Enter to increment the total.
- **System Monitor** - Monitor your CPU, RAM, disk usage, battery, and the current date and time in real time.
- **Random Number Generator** - Generate a random whole number between two specified limits, including negative numbers.
- **Dice Roller** - Roll virtual dice with customizable sides and quantities.
- **Unit Converter** - Convert between units of length, mass, and temperature.
- **Pomodoro Timer** - Set customizable work and break intervals based on the Pomodoro Technique.
- **Coin Flipper** - Flip a virtual coin.
- **Desktop shortcut setup** - Use `shortcut.bat` on Windows to create a desktop shortcut for Termyx.
- **Colour-coded output** - Colour-coded text across all tools for a more polished experience.
- **Improved navigation** - The main directory separates commands from tools and supports direct access to `changelog (cl)` and `help (h)`.
- **Interactive CLI** - Friendly input prompts with validation and tailored "again?" prompts for repeated tasks.

## What's New In 1.9.0?

### New Features
- A Windows shortcut flow has been added with `shortcut.bat`, `setup.ps1`, and `termyx.ico`.
- Stopwatch lap recording has been added with the `lap (l)` command.
- Lap times are now displayed when the stopwatch closes.
- Stopwatch command shorthands are now supported: `start (s)` | `stop (st)` | `reset (r)` | `lap (l)` | `quit (q)`.
- `q` is now supported as a shorthand for `quit` in both System Monitor and Tally Counter.

### App Improvements
- Stopwatch time is now displayed in `MM:SS` format instead of raw seconds.
- System Monitor now refreshes every 0.25 seconds instead of 0.5 seconds.
- The app now shows a time-of-day greeting on launch.
- The opening banner includes that greeting directly.
- Intro lines across tools have been rewritten to feel more personal and tool-specific.
- Again prompts across tools have been updated to better match each tool.
- When the changelog or help text is opened at startup, the app now waits for Enter before continuing to the directory.

### Scripting Improvements
- Unnecessary `ValueError` handling has been removed from the main directory loop.
- Command routing in `main.py` has been expanded to support the central `changelog` and `help` commands.
- Minor flow and formatting improvements have been made across the app.

### Bug Fixes
- `os.system("")` has been restored in `main.py` to re-enable ANSI colour handling on Windows Command Prompt.
- Stopwatch reset output now stays consistent with the new `MM:SS` display format.
- Naming remains consistent across the app, including `System Monitor` and `Coin Flipper`.

## Why Termyx?
Termyx is perfect for learners, coders, and anyone who wants quick, reliable CLI utilities without leaving the terminal. Its modular design makes it easy to extend or modify for personal needs.

## Prerequisites

To run Termyx, you will need the following:

- **Python 3.8+** - Termyx is built in Python. You can download it from [python.org](https://www.python.org/downloads/).
- **psutil** - Required for the System Monitor tool. Install it by running:
  ```bash
  pip install psutil
  ```
- **A terminal or command-line interface** - Command Prompt, PowerShell, or any CLI that can run Python scripts.

> **Note:** Termyx has been developed and tested on **Windows 10+**. It should work on macOS and Linux, but this has not been fully tested. If you run Termyx on a non-Windows system and encounter issues, please open an Issue or post in the Discord server.

## File Structure

As of version 1.9.0, Termyx is organized into a modular folder structure:

```text
Version_1.9.0-stable/
|-- setup.ps1
|-- shortcut.bat
|-- termyx.bat
|-- termyx.ico
|-- termyx.sh
`-- Termyx/
    |-- README.md
    |-- changelog.md
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
        `-- unit_conv.py
```

`main.py` is the entry point for the app. Each tool lives in its own file inside the `Tools/` folder. `termyx.bat` and `termyx.sh` are launch scripts for Windows and macOS/Linux respectively. On Windows, `shortcut.bat` can be used to create a desktop shortcut.

## How to Download

1. Go to the **Termyx releases page**.
2. Find the latest release.
3. Download the `Version_x.x.x.zip` folder.
4. Extract the `.zip` file to a location of your choice.
5. Install dependencies:
   ```bash
   pip install psutil
   ```
6. Launch the app:
   - **Windows** - double-click `termyx.bat`
   - **Windows shortcut setup** - double-click `shortcut.bat` to create a desktop shortcut
   - **macOS / Linux** - run `./termyx.sh` in your terminal (you may need to run `chmod +x termyx.sh` first)
   - **Any platform** - navigate into the `Termyx/` folder and run `python main.py`

**Note:**  
The `x.x.x` in the filename represents the version number of the application.

## Additional Notes

- Termyx runs entirely in the **terminal / command line**.
- Some features may change between versions as the app is still under development.
- If you encounter bugs or issues, please open an **Issue** on the repository or create a forum post on the Discord server.
- Always download the **latest release** to ensure you have the newest features and fixes.
- Make sure **Python is correctly installed and added to your system PATH** before running the program.

## Versioning

Termyx uses **semantic-style versioning**:

`MAJOR.MINOR.PATCH`

**Example:**  
`1.9.0`

- **MAJOR** - Major changes or large new features
- **MINOR** - Smaller feature additions or improvements
- **PATCH** - Bug fixes and minor adjustments

## License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

This means you are free to:

- Use the software
- Modify the source code
- Distribute copies
- Distribute modified versions

However, any redistributed or modified versions **must also be licensed under GPL-3.0** and include the original license.

For full details, see the `LICENSE` file included in this repository or read the license here:  
https://www.gnu.org/licenses/gpl-3.0.en.html


