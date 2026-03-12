# Termyx - Multi-Function CLI App

The app is currently on Version 1.4.0.

If you like what you see, consider joining the Discord Server at this link: https://discord.gg/eJqdyjRv

**Termyx** is a lightweight, all-in-one command-line interface (CLI) application designed for quick, practical tasks directly from your terminal. Built with Python, Termyx offers a suite of tools for everyday productivity and learning exercises, all wrapped in a fun, retro-inspired interface.

## Features
- **Stopwatch** – Track elapsed time with start, stop, and reset commands.
- **Timer** – Set a countdown timer in seconds, or use interval mode to count down from a starting number to an end number with a custom step and delay.
- **Calculator** – Perform basic arithmetic operations (+, -, *, /, **) quickly, including exponents.
- **Tally Counter** – Keep track of counts by pressing Enter to increment the total.
- **System Stats** – Monitor your CPU and RAM usage in real time, updated every 0.5 seconds.
- **Random Number Generator** – Generate a random whole number between two specified limits.
- **Easy Navigation** – Choose a tool, perform tasks, and return to the directory with simple prompts.
- **Interactive CLI** – Friendly input prompts with validation and "do again?" options for repeated tasks.
- **Help Command** – Type `help` or `h` at the startup prompt to view available tools and support links.

## Why Termyx?
Termyx is perfect for learners, coders, and anyone who wants quick, reliable CLI utilities without leaving the terminal. Its modular design makes it easy to extend or modify for personal needs.

## Prerequisites

To run Termyx, you will need the following:

- **Python 3.8+** – Termyx is built in Python. You can download it from [python.org](https://www.python.org/downloads/).
- **psutil** – Required for the System Stats tool. Install it by running:
  ```
  pip install psutil
  ```
- **A terminal or command-line interface** – Command Prompt, PowerShell, or any CLI that can run Python scripts.
- **Basic familiarity with running Python scripts** – You should know how to navigate to the correct folder and run a script using `python main.py`.

> **Note:** Termyx has been developed and tested on **Windows 10+**. It should work on macOS and Linux, but this has not been fully tested. If you run Termyx on a non-Windows system and encounter issues, please open an Issue or post in the Discord server.

## File Structure

As of version 1.4.0, Termyx is organized into a modular folder structure:

```
Version_1.4.0-stable/
├── main.py
└── Tools/
    ├── __init__.py
    ├── timer.py
    ├── stopwatch.py
    ├── calculator.py
    ├── tally.py
    ├── system_stats.py
    └── rng.py
```

`main.py` is the entry point for the app. Each tool lives in its own file inside the `Tools/` folder.

## How to Download

1. Go to the **Termyx releases page**.
2. Find the latest release.
3. Download the `Termyx v.x.x.x.zip` folder.
4. Extract the `.zip` file to a location of your choice.
5. Open your preferred terminal or command-line interface and navigate to the `Version_x.x.x-stable` folder inside the extracted zip.
6. Install dependencies:
   ```
   pip install psutil
   ```
7. Run the app:
   ```
   python main.py
   ```

**Note:**  
The `x.x.x` in the filename represents the version number of the application (for example: `Version_1.4.0-stable.zip`).

## Additional Notes

- Termyx runs entirely in the **terminal / command line**.
- Some features may change between versions as the app is still under development.
- If you encounter bugs or issues, please open an **Issue** on the repository or create a forum post on the Discord server.
- Always download the **latest release** to ensure you have the newest features and fixes.
- Make sure **Python is correctly installed and added to your system PATH** before running the program.

---

## Versioning

Termyx uses **semantic-style versioning**:

`MAJOR.MINOR.PATCH`

**Example:**  
`1.4.0`

- **MAJOR** – Major changes or large new features
- **MINOR** – Smaller feature additions or improvements
- **PATCH** – Bug fixes and minor adjustments

---

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
