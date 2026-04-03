from datetime import datetime
import os
import sys

try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False

from Tools import timer, stopwatch, calculator, tally, rng, dice, unit_conv, pom_tmr, coin_flip, settings
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET
from Tools.settings import run as settings_run
from Tools.updater import check_for_updates

if PSUTIL_AVAILABLE:
    from Tools import system_monitor
else:
    system_monitor = None

os.system("")
print("\033]0;Termyx\007", end="", flush=True)

def get_helplinks():
    commands = [
        "- Changelog (cl) - View the latest release notes inside the app.",
        "- Help (h) - View tool descriptions, colour roles, and project links.",
        "- Settings (st) - Manage theme selection and saved Pomodoro defaults.",
    ]
    tools = [
        "- Stopwatch (sw) - Track elapsed time with start, stop, and reset commands.",
        "- Timer (tmr) - Set a countdown or interval timer in minutes, perfect for short tasks or exercises.",
        "- Calculator (calc) - Perform arithmetic operations (+, -, *, /, **, //, sqrt, %) quickly, including exponents, floor division, square root, and percentage.",
        "- Tally Counter (tly) - Keep track of counts by pressing enter to increment the total.",
        "- System Monitor (sys) - Track your CPU, RAM, disk usage, and battery, updated every 0.25 seconds." if PSUTIL_AVAILABLE else None,
        "- Random Number Generator (rng) - Generate a random number between two specified limits, including negative numbers.",
        "- Dice Roller (dice) - Roll virtual dice with customizable sides and quantities.",
        "- Unit Converter (uc) - Convert between metric units of length, mass, and temperature.",
        "- Pomodoro Timer (pom) - Set work and break intervals to boost productivity.",
        "- Coin Flipper (coin) - Flip a virtual coin.",
    ]
    commands_str = "\n".join(commands)
    tools_str = "\n".join(line for line in tools if line is not None)
    return (f"""
Available Commands:

{commands_str}

Available Tools:

{tools_str}

Colour Guide:

{YELLOW}Primary{RESET} - headers, welcome messages, navigation hints and interruption messages.
{RED}Error{RESET} - errors and invalid input.
{GREEN}Success{RESET} - successful results and positive outcomes.
{CYAN}Accent{RESET} - live values and active displays.
No colour - conversational prompts and neutral messages.

Helplinks:
Join the Discord Server -> https://discord.gg/GxPxfjGAef

Check out the GitHub -> https://github.com/SS-YYC/Termyx
""")

changelog = ("""
\n
Version 1.10.1 is here with the following

New Features

- Three new themes have been added:
    - Forest - Deep greens and earthy tones. Calm and grounded.
    - Amber - Warm ambers and whites. Retro and nostalgic.
    - Dracula - Purples and greens. Dark and mysterious.

App Improvements

- Pomodoro defaults can now be changed and saved from the settings menu.
- User settings are now saved in a per-user config location, so they persist across app updates.
- Theme and Pomodoro settings now survive when users download and switch to a newer Termyx version.
- The terminal tab name now updates to show the active tool while you use it.
- A new settings menu groups theme selection and Pomodoro defaults in one place.

Scripting Improvements

- The update checker now compares version numbers safely, which avoids false update notices on newer builds.
- Update notices now show the latest available version directly in the startup message.
- Repeat prompts across the tools now use a consistent `(Y/n)` format.

Bug Fixes

- Theme changes no longer overwrite other saved settings such as Pomodoro defaults.
""")

break_msg = f"\n{YELLOW}App terminated successfully. Goodbye!{RESET}"
valid_commands = (
    "timer", "tmr",
    "stopwatch", "sw",
    "calculator", "calc",
    "tally counter", "tly",
    *(("system monitor", "sys") if PSUTIL_AVAILABLE else ()),
    "random number generator", "rng",
    "dice roller", "dice",
    "unit converter", "uc",
    "pomodoro timer", "pom",
    "coin flipper", "coin",
    "settings", "st",
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
    print(f"{YELLOW}{greeting}, and welcome to{RESET}")
    print(r"""
 _____                             
|_   _|__ _ __ _ __ ___  _   ___  __
  | |/ _ \ '__| '_ ` _ \| | | \ \/ /
  | |  __/ |  | | | | | | |_| |>  <     v.1.10.1-alpha
  |_|\___|_|  |_| |_| |_|\__, /_/\_\
                         |___/
a CLI toolkit by SS-YYC.""")

    if not PSUTIL_AVAILABLE:
        print(f"\n{RED}NOTE: The System Monitor is unavailable - it requires psutil to be installed.{RESET}")
        print(f"To enable it, run {CYAN}pip install psutil{RESET} in your terminal.\n")
    CURRENT_VERSION = "v.1.10.1-alpha"
    update = check_for_updates(CURRENT_VERSION)
    if update:
        print(f"{CYAN}A new version of Termyx is available. Latest version: {update}{RESET}")
        print(f"Download it at https://github.com/SS-YYC/Termyx/releases. \n")
    else:
        print(f"{GREEN}You are running the latest version of Termyx!{RESET}\n")    
    input("Press Enter to continue.\n> ").lower().strip()
    

    while True:
        print("\033]0;Termyx\007", end="", flush=True)
        while True:
            directory_lines = [
f"{YELLOW}Commands:{RESET}",
f"{CYAN}- Changelog (cl){RESET}",
f"{CYAN}- Help (h){RESET}",
f"{CYAN}- Settings (st){RESET}",
"---",
f"{YELLOW}Tools:{RESET}",
f"{CYAN}- Stopwatch (sw){RESET}",
f"{CYAN}- Timer (tmr){RESET}",
f"{CYAN}- Calculator (calc){RESET}",
f"{CYAN}- Tally Counter (tly){RESET}",
f"{CYAN}- System Monitor (sys){RESET}" if PSUTIL_AVAILABLE else None,
f"{CYAN}- Random Number Generator (rng){RESET}",
f"{CYAN}- Dice Roller (dice){RESET}",
f"{CYAN}- Unit Converter (uc){RESET}",
f"{CYAN}- Pomodoro Timer (pom){RESET}",
f"{CYAN}- Coin Flipper (coin){RESET}",
]

            print(f"\n{YELLOW}Directory:{RESET}")
            print("\n".join(line for line in directory_lines if line is not None))
            print()
            print(f"To quit, type {YELLOW}'quit (q)'{RESET} or press CTRL + C.")
            choice = input("> ").strip().lower()
            if choice in ("q", "quit"):
                print(f"{GREEN}Exiting the app. Thanks for using Termyx!{RESET}")
                sys.exit()
            elif choice in valid_commands:
                break
            else:
                print(f"{RED}Invalid entry.{RESET}")

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
            print(changelog)
            input("Press Enter to continue to the directory.\n")
        elif choice in ("help", "h"):
            print(get_helplinks())
            input("Press Enter to continue to the directory.\n")
        elif choice in ("settings", "st"):
            settings_run()

except (KeyboardInterrupt, EOFError):
    print(break_msg)
    sys.exit()

