from datetime import datetime
import os
import sys
CURRENT_VERSION = "v.1.11.0"
TAGLINE = "Flow State"
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
Termyx {CURRENT_VERSION} - {TAGLINE} is here with the following

New Features

- Added a Wheel Spinner tool with random-pick and elimination modes for custom option lists.
- Added calculator history so the last 5 answers are saved in config.json and remembered between sessions.
- Added a dedicated `history (h)` command in the Calculator to view saved answers on demand.

App Improvements

- Clarified prompts and status messages across the app for cleaner, more consistent wording.
- Improved repeat-prompt defaults and command exit hints so tool flow feels more consistent.
- Standardized `quit (q)` as the visible exit keybind across the app.
- Refreshed the splash screen with a cleaner welcome flow at startup.
- Updated the startup ASCII art for the new splash screen.
- Updated the startup intro with a simpler welcome line and a local date-and-time display.
- Added a saved 12-hour or 24-hour time format setting for the splash screen and System Monitor.
- Removed unnecessary repeat prompts from quick-use tools so they stay open until you choose to quit.
- Improved helplinks screen.

Scripting Improvements

- Added clean `EOFError` handling across the app so tools return more gracefully when input is closed unexpectedly.
- Standardized prompt spacing so prompts now consistently show the message, a blank line, and then `>`.
- Better System Monitor references when it's unavailable.
- Various minor scripting improvements for easier future development.

Bug Fixes

- Fixed `(Y/n)` prompts so pressing Enter now consistently uses the default `Yes` behavior.
- Fixed awkward leftover wording in a few prompts and status messages.
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
    update = check_for_updates(CURRENT_VERSION)
    if update:
        print(f"{CYAN}A new version of Termyx is available. Latest version: {update}{RESET}")
        print(f"Download it at https://github.com/SS-YYC/Termyx/releases.\n")
    else:
        print(f"{GREEN}You are running the latest version of Termyx!{RESET}\n")
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
        elif choice in ("wheel spinner", "wheel", "wh"):
            wheelspin.run()
        elif choice in ("unit converter", "uc"):
            unit_conv.run()
        elif choice in ("pomodoro timer", "pom"):
            pom_tmr.run()
        elif choice in ("coin flipper", "coin"):
            coin_flip.run()
        elif choice in ("changelog", "cl"):
            print(changelog)
            input("Press Enter to continue to the directory.\n\n> ")
        elif choice in ("help", "h"):
            print(get_helplinks())
            input("Press Enter to continue to the directory.\n\n> ")
        elif choice in ("settings", "st"):
            settings_run()

except (KeyboardInterrupt, EOFError):
    print(break_msg)
    sys.exit()