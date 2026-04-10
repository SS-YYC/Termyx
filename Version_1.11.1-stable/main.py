from datetime import datetime
import os
import sys
CURRENT_VERSION = "v.1.11.1"
TAGLINE = ""
try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False

from Tools import timer, stopwatch, calculator, tally, rng, dice, unit_conv, pom_tmr, coin_flip, settings, wheelspin
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET
from Tools.settings import run as settings_run, format_clock_time
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
        "- Settings (st) - Modify app preferences like time format, colour themes, and calculator history management.",
    ]
    tools = [
        "- Stopwatch (sw) - Track elapsed time with start, stop, and reset commands.",
        "- Timer (tmr) - Set a countdown or interval timer in minutes, perfect for short tasks or exercises.",
        "- Calculator (calc) - Perform arithmetic operations (+, -, *, /, **, //, sqrt, %) quickly, including exponents, floor division, square root, and percentage.",
        "- Tally Counter (tly) - Keep track of counts by pressing enter to increment the total.",
        "- System Monitor (sys) - Track your CPU, RAM, disk usage, and battery, updated every 0.25 seconds." if PSUTIL_AVAILABLE else f"- System Monitor (sys) (unavailable - run 'pip install psutil' to enable)",
        "- Random Number Generator (rng) - Generate a random number between two specified limits, including negative numbers.",
        "- Dice Roller (dice) - Roll virtual dice with customizable sides and quantities.",
        "- Wheel Spinner (wh) - Spin between custom options in random or elimination mode.",
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

changelog = (f"""
\n
Termyx {CURRENT_VERSION} {TAGLINE} is here with the following

New Features

- Began Phase 1 of a 2-part download overhaul, with packaged downloads and startup improvements now in place ahead of a future installer.
- Downloaded Windows builds can now be launched directly from the packaged `Termyx.exe`, with shortcut creation aimed at the packaged app instead of the source files.

App Improvements

- Standardized all general error messages to `Invalid entry.`.
- The opening banner's version and tagline text are now dynamic.
- The app will no longer notify you if you are on the latest version, but will still notify you if a new version is avaliable.
- The calculator history limit has been increased to 10 entries.
- The updater can now distinguish internet issues from other check failures and shows a clearer unavailable-status message when needed.

Scripting Improvements

- Changed the directory code to now take aliases from a dictionary.
- The terminal tab will now display `Termyx - RNG` instead of `Termyx - Random Number Generator` to better fit smaller displays.
- The coin flipper's spin time has been decreased to 1 second instead of 2.
- Various minor scripting improvements.

Bug Fixes

- The Elimination Wheel will no longer incorrectly loop and erase all values after each spin. The `Spin again (Y/n)?` message will show only on the Random Wheel.
- Fixed incorrectly decrementing times in the Pomodoro Timer by adjusting code positioning.
- Incorrect punctuation and grammar across the app has been fixed.
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
    "wheel spinner", "wheel", "wh",
    "unit converter", "uc",
    "pomodoro timer", "pom",
    "coin flipper", "coin",
    "settings", "st",
    "changelog", "cl",
    "help", "h"
)

try:

    hour = datetime.now().hour
    now = datetime.now()
    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    date_line = f"It's {format_clock_time(now)}, on the {now.day} of {now.strftime('%B')}, {now.year}."
    print(f"{YELLOW}{greeting}!{RESET}")
    print(date_line)
    print(f"{YELLOW}Welcome to{RESET}")
    print(rf"""
 ______   ______     ______     __    __     __  __     __  __   
/\__  _\ /\  ___\   /\  == \   /\ "-./  \   /\ \_\ \   /\_\_\_\  
\/_/\ \/ \ \  __\   \ \  __<   \ \ \-./\ \  \ \____ \  \/_/\_\/_    {CURRENT_VERSION}
   \ \_\  \ \_____\  \ \_\ \_\  \ \_\ \ \_\  \/\_____\   /\_\/\_\
    \/_/   \/_____/   \/_/ /_/   \/_/  \/_/   \/_____/   \/_/\/_/
    
a CLI toolkit by SS-YYC.""")

    if not PSUTIL_AVAILABLE:
        print(f"\n{RED}NOTE: The System Monitor is unavailable - it requires psutil to be installed.{RESET}")
        print(f"To enable it, run {CYAN}pip install psutil{RESET} in your terminal.\n")
    update_status, update = check_for_updates(CURRENT_VERSION)
    if update_status == "update":
        print(f"{CYAN}A new version of Termyx is available. Latest version: {update}{RESET}")
        print(f"Download it at https://github.com/SS-YYC/Termyx/releases.\n")
    elif update_status == "internet_unavailable":
        print(f"{YELLOW}Update status unavailable right now. Please check your internet connection.{RESET}\n")
    elif update_status == "unavailable":
        print(f"{YELLOW}Update status unavailable right now.{RESET}\n")
    input("Press Enter to continue.\n\n> ").lower().strip()

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
                f"{CYAN}- System Monitor (sys){RESET}" if PSUTIL_AVAILABLE else f"{CYAN}- System Monitor (sys) {RED}(unavailable){RESET}",
                f"{CYAN}- Random Number Generator (rng){RESET}",
                f"{CYAN}- Dice Roller (dice){RESET}",
                f"{CYAN}- Wheel Spinner (wh){RESET}",
                f"{CYAN}- Unit Converter (uc){RESET}",
                f"{CYAN}- Pomodoro Timer (pom){RESET}",
                f"{CYAN}- Coin Flipper (coin){RESET}",
            ]

            print(f"\n{YELLOW}Directory:{RESET}")
            print("\n".join(line for line in directory_lines if line is not None))
            print()
            print(f"To quit, type {YELLOW}'quit (q)'{RESET} or press CTRL + C.")
            choice = input("\n> ").strip().lower()
            if choice in ("q", "quit", "s", "stop"):
                print(f"{GREEN}Exiting the app. Thanks for using Termyx!{RESET}")
                sys.exit()
            elif choice in ("system monitor", "sys") and not PSUTIL_AVAILABLE:
                print(f"{RED}The System Monitor is unavailable — run 'pip install psutil' in your terminal to enable it.{RESET}")
            elif choice in valid_commands:
                break
            else:
                print(f"{RED}Invalid entry.{RESET}")

        aliases = {
            "tmr": "timer",
            "sw": "stopwatch",
            "calc": "calculator",
            "tly": "tally counter",
            "sys": "system monitor",
            "rng": "random number generator",
            "dice": "dice roller",
            "wheel": "wheel spinner", "wh": "wheel spinner",
            "uc": "unit converter",
            "pom": "pomodoro timer",
            "coin": "coin flipper",
            "st": "settings",
            "cl": "changelog",
            "h": "help",
}

        options = {
            "timer": timer.run,
            "stopwatch": stopwatch.run,
            "calculator": calculator.run,
            "tally counter": tally.run,
            "system monitor": system_monitor.run if PSUTIL_AVAILABLE else None,
            "random number generator": rng.run,
            "dice roller": dice.run,
            "wheel spinner": wheelspin.run,
            "unit converter": unit_conv.run,
            "pomodoro timer": pom_tmr.run,
            "coin flipper": coin_flip.run,
            "settings": settings_run,
            "changelog": lambda: [print(changelog), input("Press Enter to continue to the directory.\n\n> ")],
            "help": lambda: [print(get_helplinks()), input("Press Enter to continue to the directory.\n\n> ")],
        }

        resolved = aliases.get(choice, choice)
        fn = options.get(resolved)
        if fn:
            fn()

except (KeyboardInterrupt, EOFError):
    print(break_msg)
    sys.exit()
