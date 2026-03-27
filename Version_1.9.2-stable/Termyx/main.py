from datetime import datetime
import os
import sys

from Tools import timer, stopwatch, calculator, tally, system_monitor, rng, dice, unit_conv, pom_tmr, coin_flip
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET

os.system("")

changelog = ("""
\n
Version 1.9.2 is here with the following updates:

App Improvements

- The startup banner now correctly reflects the current version number.
- System Monitor help text now correctly reports its 0.25 second refresh rate.
- Shortcut setup messaging now better reflects current Windows taskbar behavior.
- Release information across the app is now more consistent and easier to follow.

Scripting Improvements:

- Minor wording and release-text cleanup has been carried out across the alpha and stable builds.
- Embedded version text has been brought in line with the current release.
- Supporting setup text has been adjusted to better match real application behavior.

Bug Fixes:

- The splash screen no longer shows the previous version number.
- System Monitor no longer advertises an outdated refresh speed in the help text.
- The shortcut script no longer promises taskbar pinning behavior that may not work as expected.
             
Press Enter to continue to the directory.

""")
helplinks = ("""
Available Tools:
             
- Stopwatch (sw) - Track elapsed time with start, stop, and reset commands.
- Timer (tmr) - Set a countdown or interval timer in minutes, perfect for short tasks or exercises.
- Calculator (calc) - Perform arithmetic operations (+, -, *, /, **, //, sqrt, %) quickly, including exponents, floor division, square root, and percentage.
- Tally Counter (tly) - Keep track of counts by pressing enter to increment the total.
- System Monitor (sys) - Track your CPU, RAM, disk usage, and battery, updated every 0.25 seconds.
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
  | |  __/ |  | | | | | | |_| |>  <     v.1.9.2
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

