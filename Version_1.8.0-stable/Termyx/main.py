import sys

from Tools import timer, stopwatch, calculator, tally, system_stats, rng, dice, unit_conv, pom_tmr, coin_flip
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET
import os
os.system("")

changelog = ("""
\n
Added in Version 1.8.0:

- A new Coin Flip tool has been added, allowing users to flip a virtual coin with a spinner animation.
- Coloured text has been added across the app - see below. This should work across all operating systems.

Colour Guide:

- Yellow — headers, welcome messages, navigation hints and interruption messages.
- Red — errors and invalid input.
- Green — successful results and positive outcomes.
- Cyan — live values and active displays.
- No colour — conversational prompts and neutral messages.

Bug Fixes and Scripting Improvements:

- The Pomodoro Timer's 3 second countdown is now dynamic, counting down visually instead of showing a static message.
- A missing comma in valid_commands caused the Pomodoro Timer shorthand to silently break. This has been fixed.
- The Pomodoro Timer now displays a productivity summary at the end of a session, showing total time spent working and on breaks.
- Fixed a crash message that occurred when hitting CTRL + C in the Pomodoro Timer.
- Splash screen and intro sequence overhaul.
- Changes to user flow and sequencing across the app.
- Code optimizations across various parts of the app.
""")

helplinks = ("""
Available Tools:
             
- Stopwatch (sw) - Track elapsed time with start, stop, and reset commands.
- Timer (tmr) - Set a countdown or interval timer in minutes, perfect for short tasks or exercises.
- Calculator (calc) - Perform arithmetic operations (+, -, *, /, **, //, sqrt, %) quickly, including exponents, floor division, square root, and percentage.
- Tally Counter (tly) - Keep track of counts by pressing enter to increment the total.
- System Stats (sys) - Track your CPU, RAM, disk usage, and battery, updated every 0.5 seconds.
- Random Number Generator (rng) - Generate a random number between two specified limits, including negative numbers.
- Dice Roller (dice) - Roll virtual dice with customizable sides and quantities.
- Unit Converter (uc) - Convert between metric units of length, mass, and temperature.
- Pomodoro Timer (pom) - Set work and break intervals to boost productivity.
- Coin Flip (coin) - Flip a virtual coin.
             

Helplinks:
Join the Discord Server -> https://discord.gg/GxPxfjGAef

Check out the GitHub -> https://github.com/SS-YYC/Termyx
             
Colour Guide:

- Yellow — headers, welcome messages, navigation hints and interruption messages.
- Red — errors and invalid input.
- Green — successful results and positive outcomes.
- Cyan — live values and active displays.
- No colour — conversational prompts and neutral messages.
""")

break_msg = f"\n{YELLOW}App terminated successfully. Goodbye!{RESET}"
valid_commands = (
    "timer", "tmr",
    "stopwatch", "sw",
    "calculator", "calc",
    "tally counter", "tly",
    "system stats", "sys",
    "random number generator", "rng",
    "dice roller", "dice",
    "unit converter", "uc",
    "pomodoro timer", "pom",
    "coin flip", "coin"
)

try:
    print(r"""
          
Welcome to
 _____                              
|_   _|__ _ __ _ __ ___  _   ___  __
  | |/ _ \ '__| '_ ` _ \| | | \ \/ /
  | |  __/ |  | | | | | | |_| |>  < 
  |_|\___|_|  |_| |_| |_|\__, /_/\_\  v.1.8.0
                         |___/ 
a CLI toolkit by SS-YYC.""")

    print("Welcome to Termyx! Press CTRL + C at any time to quit.")
    cl = input("Press Enter to continue. Commands: changelog (cl) | help (h)\n> ").lower().strip()
    if cl in ("changelog", "cl"):
        print(changelog)
    elif cl in ("help", "h"):
        print(helplinks)

    while True:
        while True:
            try:
                print(f"\n{YELLOW}Directory:{RESET}")
                print(f"""
{CYAN}- Stopwatch (sw){RESET}
{CYAN}- Timer (tmr){RESET}
{CYAN}- Calculator (calc){RESET}
{CYAN}- Tally Counter (tly){RESET}
{CYAN}- System Stats (sys){RESET}
{CYAN}- Random Number Generator (rng){RESET}
{CYAN}- Dice Roller (dice){RESET}
{CYAN}- Unit Converter (uc){RESET}
{CYAN}- Pomodoro Timer (pom){RESET}
{CYAN}- Coin Flip (coin){RESET}
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
            except ValueError:
                print(f"{RED}One of your inputs is not recognized by the system.{RESET}")

        # Route to the correct tool
        if choice in ("timer", "tmr"):
            timer.run()
        elif choice in ("stopwatch", "sw"):
            stopwatch.run()
        elif choice in ("calculator", "calc"):
            calculator.run()
        elif choice in ("tally counter", "tly"):
            tally.run()
        elif choice in ("system stats", "sys"):
            system_stats.run()
        elif choice in ("random number generator", "rng"):
            rng.run()
        elif choice in ("dice roller", "dice"):
            dice.run()
        elif choice in ("unit converter", "uc"):
            unit_conv.run()
        elif choice in ("pomodoro timer", "pom"):
            pom_tmr.run()
        elif choice in ("coin flip", "coin"):
            coin_flip.run()

except (KeyboardInterrupt, EOFError):
    print(break_msg)
    sys.exit()