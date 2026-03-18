import sys

from Tools import timer, stopwatch, calculator, tally, system_stats, rng, dice, unit_conv, pom_tmr

changelog = ("""
\n
Changelog:

Improved in Version 1.7.1:
             
- Improved CTRL + C handling across each tool individually. You can now hit CTRL + C to exit out of a tool and return to the directory, or hit it twice to exit the app entirely. 
- UI consistency changes across the app.
- UI and intro sequence improvements
- Unnecessary lines of code have been removed
- Various missing shorthands have been added
                  
""")

helplinks = ("""
Available Tools:
             
- Stopwatch (sw) – Track elapsed time with start, stop, and reset commands.
- Timer (tmr) – Set a countdown or interval timer in minutes, perfect for short tasks or exercises.
- Calculator (calc) – Perform arithmetic operations (+, -, *, /, **, //, sqrt, %) quickly, including exponents, floor division, square root, and percentage.
- Tally Counter (tly) – Keep track of counts by pressing enter to increment the total.
- System Stats (sys) – Track your CPU, RAM, disk usage, and battery, updated every 0.5 seconds.
- Random Number Generator (rng) – Generate a random number between two specified limits, including negative numbers.
- Dice Roller (dice) – Roll virtual dice with customizable sides and quantities.
- Unit Converter (uc) – Convert between metric units of length, mass, and temperature.
- Pomodoro Timer (pom) – Set work and break intervals to boost productivity.
             

Helplinks:
Join the Discord Server -> https://discord.gg/GxPxfjGAef

Check out the GitHub -> https://github.com/SS-YYC/Termyx
""")

break_msg = "\nApp terminated successfully. Goodbye!"

directory_disp = (
    "timer (tmr)",
    "stopwatch (sw)",
    "calculator (calc)",
    "tally counter (tly)",
    "system stats (sys)",
    "random number generator (rng)",
    "dice roller (dice)",
    "unit converter (uc)",
    "pomodoro timer (pom)"
)

valid_commands = (
    "timer", "tmr",
    "stopwatch", "sw",
    "calculator", "calc",
    "tally counter", "tly",
    "system stats", "sys",
    "random number generator", "rng",
    "dice roller", "dice",
    "unit converter", "uc",
    "pomodoro timer", "pom"
)

try:
    print(r"""
 _____                              
|_   _|__ _ __ _ __ ___  _   ___  __
  | |/ _ \ '__| '_ ` _ \| | | \ \/ /
  | |  __/ |  | | | | | | |_| |>  < 
  |_|\___|_|  |_| |_| |_|\__, /_/\_\  v.1.7.1
                         |___/                                                                                                
Termyx - made by SS-YYC. Licensed under GPL-3.0. Feel free to use and modify this code at your own leisure.                                   
                 """)

    print("Welcome to Termyx!")
    print("Please follow the instructions below to use the app! To quit at any time, hit CTRL + C on your keyboard.")

    cl = input("Hit Enter to proceed. To view the changelog, type 'changelog' or 'cl'. For help and support, type 'help' or 'h'.\n> ")
    if cl.lower().strip() in ("changelog", "cl"):
        print(changelog)
    if cl.lower().strip() in ("help", "h"):
        print(helplinks)

    while True:
        # Tool selection
        while True:
            try:
                print(f"\nPlease select the tool you'll be using today out of these options: ")
                print("""
Available Tools:
             
- Stopwatch (sw)
- Timer (tmr)
- Calculator (calc)
- Tally Counter (tly)
- System Stats (sys)
- Random Number Generator (rng)
- Dice Roller (dice)
- Unit Converter (uc)
- Pomodoro Timer (pom)
""")
                choice = input("> ")
                if choice.lower().strip() in valid_commands:
                    break
                else:
                    print("Invalid entry.")
            except ValueError:
                print("One of your inputs is not recognized by the system.")

        # Route to the correct tool
        if choice.lower().strip() in ("timer", "tmr"):
            timer.run()
        elif choice.lower().strip() in ("stopwatch", "sw"):
            stopwatch.run()
        elif choice.lower().strip() in ("calculator", "calc"):
            calculator.run()
        elif choice.lower().strip() in ("tally counter", "tly"):
            tally.run()
        elif choice.lower().strip() in ("system stats", "sys"):
            system_stats.run()
        elif choice.lower().strip() in ("random number generator", "rng"):
            rng.run()
        elif choice.lower().strip() in ("dice roller", "dice"):
            dice.run()
        elif choice.lower().strip() in ("unit converter", "uc"):
            unit_conv.run()
        elif choice.lower().strip() in ("pomodoro timer", "pom"):
            pom_tmr.run()

        # Return to directory?
        directoryReturn = input("Run the directory again? (y/n):\n> ")
        if directoryReturn.strip().lower() in ("y", "yes"):
            continue
        else:
            print("Thanks for using the app! To report any bugs, join the Discord or report an issue on GitHub.")
            break

except (KeyboardInterrupt, EOFError):
    print(break_msg)
    sys.exit()