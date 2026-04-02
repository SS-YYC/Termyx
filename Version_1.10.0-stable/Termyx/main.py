from datetime import datetime
import os
import sys

try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False

from Tools import timer, stopwatch, calculator, tally, rng, dice, unit_conv, pom_tmr, coin_flip
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET, select_theme
from Tools.updater import check_for_updates

if PSUTIL_AVAILABLE:
    from Tools import system_monitor
else:
    system_monitor = None

os.system("")
print("\033]0;Termyx\007", end="", flush=True)



def get_helplinks():
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
    tools_str = "\n".join(line for line in tools if line is not None)
    return (f"""
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
Version 1.10.0 is here with the following

New Features

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

App Improvements

- The startup greeting now uses the standard primary colour for better visibility.
- `psutil` is now no longer a dependency to run the entire app.
    - All references to the system monitor will disappear if `psutil` isn't installed.
    - Run `pip install psutil` in your terminal to enable it.
    - If `psutil` isn't installed, installation instructions will be displayed upon startup.
- The terminal tab name will now change to Termyx upon startup. This will be expanded to individual tools soon.

Scripting Improvements

- The startup changelog path now correctly prints the changelog before waiting for Enter.
- The startup help path now correctly prints the help text before waiting for Enter.
- Return-to-directory messaging is correctly shown as a separate prompt after startup help or changelog text.
- Directory changelog and help options print correctly with `input()` removed to avoid confusion with prompts.
- Redundant opening commands have been removed - these can still be accessed from the directory.

Bug Fixes

- Fixed startup help and changelog screens being passed directly into `input()`, which could make their prompts less clear.
- The encoding of `main.py` has been changed from UTF-8 with BOM to UTF-8 to avoid unexpected `SyntaxError` warnings on older versions of Python.
- Remaining Python source files have been standardized to UTF-8 without BOM for consistency and cleaner compatibility across tools and Python versions.
- Misplaced corrupted Mojibake across the app has been removed.
- Indentation, stripping and newline errors have been fixed in the dice roller.
- Fixed the Pomodoro summary showing the wrong number of short and long breaks after a completed session.
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
    "theme", "th",
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
  | |  __/ |  | | | | | | |_| |>  <     v.1.10.0-alpha
  |_|\___|_|  |_| |_| |_|\__, /_/\_\
                         |___/
a CLI toolkit by SS-YYC.""")

    if not PSUTIL_AVAILABLE:
        print(f"\n{RED}NOTE: The System Monitor is unavailable - it requires psutil to be installed.{RESET}")
        print(f"To enable it, run {CYAN}pip install psutil{RESET} in your terminal.\n")
    CURRENT_VERSION = "v.1.10.0"
    update = check_for_updates(CURRENT_VERSION)
    if update:
        print(f"{CYAN}A new version of Termyx is available: {update}{RESET}")
        print(f"Download it at https://github.com/SS-YYC/Termyx/releases. \n")
    else:
        print(f"{GREEN}You are running the latest version of Termyx!{RESET}\n")    
    input("Press Enter to continue.\n> ").lower().strip()
    

    while True:
        while True:
            directory_lines = [
f"{YELLOW}Commands:{RESET}",
f"{CYAN}- Changelog (cl){RESET}",
f"{CYAN}- Help (h){RESET}",
f"{CYAN}- Theme Selection (th){RESET}",
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
        elif choice in ("theme", "th"):
            select_theme()

except (KeyboardInterrupt, EOFError):
    print(break_msg)
    sys.exit()
