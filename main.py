import sys

from Tools import timer, stopwatch, calculator, tally, system_stats, rng, dice, unit_conv

changelog = ("""
\n
Changelog:

Added in Version 1.6.0:

- A unit conversion tool, allowing users to convert between various units of length, mass, and temperature.
- Floor division (// operator) has been added to the calculator, allowing users to perform integer division and obtain the quotient without the remainder.
- System Stats improvements:
    - Disk usage has been added to the system stats readout.
    - Battery status has been added to the system stats readout, including charge percentage and plugged in status. If no battery is detected, the battery stat is hidden.
    - The current date and time are now displayed above the stats readout in DD/MM/YYYY format.

And the following bug fixes and scripting improvements:
- 'Again' logic has been improved.
- Scripting inprovements in the tally counter.
- Scripting improvements in the calculator: 
    - Percentages with the base of 0 are now allowed (why would you want to do that lol).
    - A zero-check bug has been fixed.
- RNG improvements:
    - It is now clear that negative numbers are allowed to be used.
- Code optimizations across various tools.

Coming soon:
- A pomodoro timer tool, allowing users to set work and break intervals to boost productivity.
                  
""")

helplinks = ("""
Available Tools:
             
- Stopwatch – Track elapsed time with start, stop, and reset commands.
- Timer – Set a countdown or interval timer in seconds, perfect for short tasks or exercises.
- Calculator – Perform arithmetic operations (+, -, *, /, **, sqrt, %) quickly.
- Tally Counter – Keep track of counts by pressing enter to increment the total.
- System Stats – Track your CPU and RAM usage, updated to the nearest second.  
- Random Number Generator – Generate a random number between two specified limits.       
- Dice Roller – Roll virtual dice with customizable sides and quantities.
- Unit Converter – Convert between units of length, mass, and temperature.



Helplinks:
Join the Discord Server -> https://discord.gg/eJqdyjRv

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
    "unit converter (uc)"
)

valid_commands = (
    "timer", "tmr",
    "stopwatch", "sw",
    "calculator", "calc",
    "tally counter", "tly",
    "system stats", "sys",
    "random number generator", "rng",
    "dice roller", "dice",
    "unit converter", "uc"
)

try:
    print(r"""
 _____                              
|_   _|__ _ __ _ __ ___  _   ___  __
  | |/ _ \ '__| '_ ` _ \| | | \ \/ /
  | |  __/ |  | | | | | | |_| |>  < 
  |_|\___|_|  |_| |_| |_|\__, /_/\_\  v.1.6.0
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
                choice = input(f"\nPlease select the tool you'll be using today out of these options: {', '.join(directory_disp)}.\n> ")
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