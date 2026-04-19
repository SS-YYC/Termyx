from datetime import datetime
import os
import sys
CURRENT_VERSION = "v.1.12.1"
TAGLINE = "\b"
try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False

from Tools import timer, stopwatch, calculator, tally, rng, dice, unit_conv, pom_tmr, coin_flip, settings, wheelspin, password_gen
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET
from Tools.settings import run as settings_run, format_clock_time, load_startup_behaviour, get_directory_lines
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
        "- Calculator (calc) - Evaluate full expressions with arithmetic, brackets, constants, trigonometric functions, logs, square roots, and saved answer history.",
        "- Tally Counter (tly) - Keep track of counts by pressing enter to increment the total.",
        "- System Monitor (sys) - Track your CPU, RAM, disk usage, and battery, updated every 0.25 seconds." if PSUTIL_AVAILABLE else f"{RED}- System Monitor (sys) (unavailable - run 'pip install psutil' to enable){RESET}",
        "- Random Number Generator (rng) - Generate a random number between two specified limits, including negative numbers.",
        "- Dice Roller (dice) - Roll virtual dice with customizable sides and quantities.",
        "- Wheel Spinner (wh) - Spin between custom options in random or elimination mode.",
        "- Unit Converter (uc) - Convert between metric units of length, mass, and temperature.",
        "- Pomodoro Timer (pom) - Set work and break intervals to boost productivity.",
        "- Coin Flipper (coin) - Flip a virtual coin.",
        "- Password Generator (pwd) - Generate secure, random passwords with customizable options.",
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

about = (
    " ______   ______     ______     __    __     __  __     __  __   \n"
    "/\\__  _\\ /\\  ___\\   /\\  == \\   /\\ \"-./  \\   /\\ \\_\\ \\   /\\_\\_\\_\\  \n"
    f"\\/_/\\ \\/ \\ \\  __\\   \\ \\  __<   \\ \\ \\-./\\ \\  \\ \\____ \\  \\/_/\\_\\/_    {CURRENT_VERSION}\n"
    "   \\ \\_\\  \\ \\_____\\  \\ \\_\\ \\_\\  \\ \\_\\ \\ \\_\\  \\/\\_____\\   /\\_\\/\\_\\\n"
    "    \\/_/   \\/_____/   \\/_/ /_/   \\/_/  \\/_/   \\/_____/   \\/_/\\/_/\n"
    "\n"
    "a CLI toolkit by SS-YYC.\n"
    "\n"
    "Termyx is licensed under GPL-3.0. View the source code and license details at https://github.com/SS-YYC/Termyx/blob/main/LICENSE.\n"
    "Feel free to use, edit and modify this code for any reason.\n"
    "If you want to contribute, report a bug, or request a feature, please open an issue or submit a pull request on GitHub.\n"
)

changelog = (f"""

Termyx {CURRENT_VERSION} {TAGLINE} is here with the following updates and improvements:

App Improvements

- A confirmation prompt has been added to destructive actions like config resetting.

Bug Fixes

- Stopwatch names resetting incorrectly have been fixed.
- `stop (s)` is no longer accepted in place of `quit (q)` in the directory to avoid future conflicting prompts.
""")

break_msg = f"\n{YELLOW}App terminated successfully. Goodbye!{RESET}"
COMMAND_ALIASES = {
    "timer": "timer",
    "tmr": "timer",
    "stopwatch": "stopwatch",
    "sw": "stopwatch",
    "calculator": "calculator",
    "calc": "calculator",
    "tally counter": "tally counter",
    "tally": "tally counter",
    "tly": "tally counter",
    "system monitor": "system monitor",
    "sys monitor": "system monitor",
    "monitor": "system monitor",
    "sys": "system monitor",
    "random number generator": "random number generator",
    "number generator": "random number generator",
    "random number gen": "random number generator",
    "random gen": "random number generator",
    "rng": "random number generator",
    "dice roller": "dice roller",
    "die roller": "dice roller",
    "die": "dice roller",
    "dice": "dice roller",
    "wheel spinner": "wheel spinner",
    "spin a wheel": "wheel spinner",
    "wheel spin": "wheel spinner",
    "wheelspinner": "wheel spinner",
    "wheel": "wheel spinner",
    "wh": "wheel spinner",
    "unit converter": "unit converter",
    "units converter": "unit converter",
    "converter": "unit converter",
    "unit conv": "unit converter",
    "uc": "unit converter",
    "pomodoro timer": "pomodoro timer",
    "pomtimer": "pomodoro timer",
    "pom timer": "pomodoro timer",
    "pomodoro": "pomodoro timer",
    "pom": "pomodoro timer",
    "coin flipper": "coin flipper",
    "flip a coin": "coin flipper",
    "coinflip": "coin flipper",
    "coin flip": "coin flipper",
    "coin": "coin flipper",
    "password generator": "password generator",
    "password gen": "password generator",
    "pass gen": "password generator",
    "passgen": "password generator",
    "pwd gen": "password generator",
    "pwdgen": "password generator",
    "pwd": "password generator",
    "pass": "password generator",
    "password": "password generator",
    "settings": "settings",
    "st": "settings",
    "changelog": "changelog",
    "cl": "changelog",
    "help": "help",
    "h": "help",
    "about": "about",
    "abt": "about",
    "a": "about",
}

try:
    
    startup_behaviour = load_startup_behaviour()
    if startup_behaviour == "skip_splash":
        print(f"{YELLOW}Welcome to Termyx!{RESET}")
    else:
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
        print(
            " ______   ______     ______     __    __     __  __     __  __   \n"
            "/\\__  _\\ /\\  ___\\   /\\  == \\   /\\ \"-./  \\   /\\ \\_\\ \\   /\\_\\_\\_\\  \n"
            f"\\/_/\\ \\/ \\ \\  __\\   \\ \\  __<   \\ \\ \\-./\\ \\  \\ \\____ \\  \\/_/\\_\\/_    {CURRENT_VERSION}\n"
            "   \\ \\_\\  \\ \\_____\\  \\ \\_\\ \\_\\  \\ \\_\\ \\ \\_\\  \\/\\_____\\   /\\_\\/\\_\\\n"
            "    \\/_/   \\/_____/   \\/_/ /_/   \\/_/  \\/_/   \\/_____/   \\/_/\\/_/\n"
            "\n"
            "a CLI toolkit by SS-YYC."
        )

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
                f"{CYAN}- About (a){RESET}",
                "---",
                f"{YELLOW}Tools:{RESET}",
                *get_directory_lines(PSUTIL_AVAILABLE),
            ]

            print(f"\n{YELLOW}Directory:{RESET}")
            print("\n".join(line for line in directory_lines if line is not None))
            print()
            print(f"To quit, type {YELLOW}'quit (q)'{RESET} or press CTRL + C.")
            choice = input("\n> ").strip().lower()
            if choice in ("q", "quit"):
                print(f"{GREEN}Exiting the app. Thanks for using Termyx!{RESET}")
                sys.exit()
            elif choice in ("system monitor", "sys") and not PSUTIL_AVAILABLE:
                print(f"{RED}The System Monitor is unavailable — run 'pip install psutil' in your terminal to enable it.{RESET}")
            elif choice in COMMAND_ALIASES:
                break
            else:
                print(f"{RED}Invalid entry.{RESET}")

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
            "password generator": password_gen.run,
            "settings": settings_run,
            "changelog": lambda: [print(changelog), input("Press Enter to continue to the directory.\n\n> ")],
            "help": lambda: [print(get_helplinks()), input("Press Enter to continue to the directory.\n\n> ")],
            "about": lambda: [print(about), input("Press Enter to continue to the directory.\n\n> ")],
        }

        resolved = COMMAND_ALIASES.get(choice)
        fn = options.get(resolved)
        if fn:
            fn()

except (KeyboardInterrupt, EOFError):
    print(break_msg)
    sys.exit()
