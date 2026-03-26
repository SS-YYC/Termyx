from datetime import datetime
import os
import sys

from Tools import timer, stopwatch, calculator, tally, system_monitor, rng, dice, unit_conv, pom_tmr, coin_flip
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET

os.system("")

changelog = ("""
\n
Version 1.9.0 - Rewired
is here with the following updates:

New Features

- A new `shortcut.bat` file has been added to create a desktop shortcut for Termyx.
- `setup.ps1` and `termyx.ico` have been added to support that shortcut flow on Windows.
- Stopwatch lap times have been added with the new `lap (l)` command.
- All recorded lap times are now displayed when the stopwatch is closed.
- Stopwatch commands now support shorthands: `start (s)` | `stop (st)` | `reset (r)` | `lap (l)` | `quit (q)`.
- `q` is now supported as a shorthand for `quit` in System Monitor.
- `q` is now supported as a shorthand for `quit` in Tally Counter.

App Improvements

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

Scripting Improvements:

- Unnecessary `ValueError` handling has been removed from the main directory loop.
- Command routing in `main.py` has been expanded to support the new central `changelog` and `help` commands.
- Minor flow and formatting improvements have been made across the app.

Bug Fixes:

- `os.system("")` has been restored in `main.py` to re-enable ANSI colour handling on Windows Command Prompt.
- Stopwatch reset output now stays consistent with the new MM:SS display format.
- Previous naming changes such as `System Monitor` and `Coin Flipper` remain consistent throughout the app.
             
Press Enter to continue to the directory.

""")
helplinks = ("""
Available Tools:
             
- Stopwatch (sw) - Track elapsed time with start, stop, and reset commands.
- Timer (tmr) - Set a countdown or interval timer in minutes, perfect for short tasks or exercises.
- Calculator (calc) - Perform arithmetic operations (+, -, *, /, **, //, sqrt, %) quickly, including exponents, floor division, square root, and percentage.
- Tally Counter (tly) - Keep track of counts by pressing enter to increment the total.
- System Monitor (sys) - Track your CPU, RAM, disk usage, and battery, updated every 0.5 seconds.
- Random Number Generator (rng) - Generate a random number between two specified limits, including negative numbers.
- Dice Roller (dice) - Roll virtual dice with customizable sides and quantities.
- Unit Converter (uc) - Convert between metric units of length, mass, and temperature.
- Pomodoro Timer (pom) - Set work and break intervals to boost productivity.
- Coin Flipper (coin) - Flip a virtual coin.
             

Helplinks:
Join the Discord Server -> https://discord.gg/GxPxfjGAef

Check out the GitHub -> https://github.com/SS-YYC/Termyx
             
Colour Guide:

- Yellow - headers, welcome messages, navigation hints and interruption messages.
- Red - errors and invalid input.
- Green - successful results and positive outcomes.
- Cyan - live values and active displays.
- No colour - conversational prompts and neutral messages.
             
Press Enter to continue to the directory.
""")

break_msg = f"\n{YELLOW}App terminated successfully. Goodbye!{RESET}"
valid_commands = (
    "timer", "tmr",
    "stopwatch", "sw",
    "calculator", "calc",
    "tally counter", "tly",
    "system monitor", "sys",
    "random number generator", "rng",
    "dice roller", "dice",
    "unit converter", "uc",
    "pomodoro timer", "pom",
    "coin flipper", "coin",
    "changelog", "cl",
    "help", "h"
)

try:

    hour = datetime.now().hour
    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    print(rf"""
          
{greeting}, and welcome to
 _____                              
|_   _|__ _ __ _ __ ___  _   ___  __
  | |/ _ \ '__| '_ ` _ \| | | \ \/ /
  | |  __/ |  | | | | | | |_| |>  <     v.1.9.0
  |_|\___|_|  |_| |_| |_|\__, /_/\_\
                         |___/
a CLI toolkit by SS-YYC.""")

    
    cl = input("Press Enter to continue. Commands: changelog (cl) | help (h)\n> ").lower().strip()
    if cl in ("changelog", "cl"):
        input(changelog)
    elif cl in ("help", "h"):
        input(helplinks)

    while True:
        while True:
            print(f"\n{YELLOW}Directory:{RESET}")
            print(f"""
{YELLOW}Commands:{RESET}
{CYAN}- Changelog (cl){RESET}
{CYAN}- Help (h){RESET}
---
{YELLOW}Tools:{RESET}
{CYAN}- Stopwatch (sw){RESET}
{CYAN}- Timer (tmr){RESET}
{CYAN}- Calculator (calc){RESET}
{CYAN}- Tally Counter (tly){RESET}
{CYAN}- System Monitor (sys){RESET}
{CYAN}- Random Number Generator (rng){RESET}
{CYAN}- Dice Roller (dice){RESET}
{CYAN}- Unit Converter (uc){RESET}
{CYAN}- Pomodoro Timer (pom){RESET}
{CYAN}- Coin Flipper (coin){RESET}
""")
            print(f"To quit, type {YELLOW}'quit (q)'{RESET} or press CTRL + C.")
            choice = input("> ").strip().lower()
            if choice in ("q", "quit"):
                print(f"{GREEN}Exiting the app. Thanks for using Termyx!{RESET}")
                sys.exit()
            elif choice in valid_commands:
                break
            else:
                print(f"{RED}Invalid entry.{RESET}")

        # Route to the correct tool
        if choice in ("timer", "tmr"):
            timer.run()
        elif choice in ("stopwatch", "sw"):
            stopwatch.run()
        elif choice in ("calculator", "calc"):
            calculator.run()
        elif choice in ("tally counter", "tly"):
            tally.run()
        elif choice in ("system monitor", "sys"):
            system_monitor.run()
        elif choice in ("random number generator", "rng"):
            rng.run()
        elif choice in ("dice roller", "dice"):
            dice.run()
        elif choice in ("unit converter", "uc"):
            unit_conv.run()
        elif choice in ("pomodoro timer", "pom"):
            pom_tmr.run()
        elif choice in ("coin flipper", "coin"):
            coin_flip.run()
        elif choice in ("changelog", "cl"):
            input(changelog)
        elif choice in ("help", "h"):
            input(helplinks)

except (KeyboardInterrupt, EOFError):
    print(break_msg)
    sys.exit()

