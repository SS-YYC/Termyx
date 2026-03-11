import time
import sys
import threading
import psutil

changelog = ("""
\n
Changelog:

Added in Version 1.3.2:
             
• A new system stats function has been added. This will show your RAM and CPU usage statistics, updated each second.
• Splash screen changes.

And the following bug fixes:
             
• Bugs with the CTRL + C keybind not working in parts of the app have been fixed.

In the Works:
• A new GUI to interact with the app.
• A new 'help' command to view helplinks and a slimmed UX guide.
• Termyx has officially hit 300 lines of code! To future-proof the app, I will be rescripting Termyx in the near future. This will also see more source code added to GitHub.
""")

helplinks = ("""
Helplinks:
Join the Discord Server -> https://discord.gg/eJqdyjRv

Check out the GitHub -> https://github.com/SS-YYC/Termyx
""")


break_msg = "\nApp terminated successfully. Goodbye!"
running = False
run = True
elapsed = 0
def stopwatch():
    global elapsed, running, exit_program
    while not exit_program:
        if running:
            time.sleep(1)
            if not running:
                continue
            elapsed += 1
            print(f"\rElapsed: {elapsed} seconds ", end="", flush=True)
        else:
            time.sleep(0.1)

def system_monitor():
    global monitor_running

    psutil.cpu_percent(None)
    time.sleep(0.5)

    while monitor_running:
        cpu = psutil.cpu_percent(None)
        ram = psutil.virtual_memory().percent
        print(f"\rCPU: {cpu}% | RAM: {ram}%   ", end="", flush=True)
        time.sleep(1)
#beginning credits/intro
try:
       print(r"""
 _____                              
|_   _|__ _ __ _ __ ___  _   ___  __
  | |/ _ \ '__| '_ ` _ \| | | \ \/ /
  | |  __/ |  | | | | | | |_| |>  < 
  |_|\___|_|  |_| |_| |_|\__, /_/\_\  v.1.3.2
                         |___/                                                                                                
Termyx - made by SS-YYC. Licensed under GPL-3.0. Feel free to use and modify this code at your own leisure.                                   
                     """)

       print ("Welcome to Termyx!")
       print ("Please follow the instructions below to use the app! To quit at any time, hit CTRL + C on your keyboard.")
       print (helplinks)

       cl = input ("Hit Enter to proceed. To view the changelog, type 'changelog' or 'cl'. ")
       if cl.lower().strip() in ("changelog", "cl"):
              print(changelog)
       else: 
              pass

       #variable declaration
       directory_disp = ("counter (ctr)", "timer (tmr)", "stopwatch (sw)", "calculator (calc)", "tally counter (tly)", "system stats (sys)")
       valid_commands = (
       "counter", "ctr",
       "timer", "tmr",
       "stopwatch", "sw",
       "calculator", "calc",
       "tally counter", "tly",
       "system stats", "sys"
       )
       while run == True:
                     #Asks the user which of the avaliable tools they'd like to use.
                     while True:
                            try:
                                   choice = input(f"\nPlease select the tool you'll be using today out of these options: {(", ".join(directory_disp))}.\n> ")
                                   if choice.lower().strip() in valid_commands:
                                          break
                                   else:
                                          print("Invalid entry.")
                                          continue
                            except ValueError:
                                   print("One of your inputs is not recognized by the system.")
                                   continue

                     if choice.lower().strip() in ("timer", "tmr"): #Timer Component
                            while True:
                                   try:
                                          timedFrom = int(input("Please enter the duration of your timer in seconds: "))
                                   except ValueError:
                                          print("One of your inputs could not be recognized! Please try again.")
                                          continue

                                   if timedFrom <= 0:
                                          print("Please enter a positive number greater than 0.")
                                          continue

                                   while timedFrom > 0:
                                          print(f"\r{timedFrom} ", end="", flush=True)
                                          timedFrom -= 1
                                          time.sleep(1)

                                   print()

                                   print("Completed!")
                                   for i in range(5):
                                          print("\a", end="", flush=True)
                                          time.sleep(1)
                                   again = input("Do this again? (y/n):\n> ").lower()
                                   if again.lower().strip() != "y":
                                                 break

                     elif choice.lower().strip() in ("counter", "ctr"): #Counter
                            while True:
                                   try: 
                                          startNumber = float(input("\nPlease enter the starting number here:\n> "))
                                          endNumber = float(input("Please enter the end number (the number at which the counter ends):\n> "))
                                          if startNumber == endNumber:
                                                 print("The start and end numbers must be different!")
                                                 continue
                                          interval = float(input("Please enter the interval at which the counter should count by:\n> "))
                                          delay = float(input("Please enter the delay between counts (secs).\n> "))
                                   except ValueError:
                                          print("Please enter an number greater than 0.")
                                          continue
                                   if interval <= 0:
                                          print("Interval must be a number greater than 0.")
                                          continue

                                   epsilon = 1e-9

                                   if startNumber > endNumber:
                                          while startNumber + epsilon > endNumber:
                                                 print(startNumber)
                                                 startNumber -= interval
                                                 time.sleep(delay)
                                   else:  
                                          while startNumber - epsilon < endNumber:
                                                 print(startNumber)
                                                 startNumber += interval
                                                 time.sleep(delay)
                                   if abs(startNumber - endNumber) > epsilon:
                                          print(endNumber)

                                   again = input("Do this again? (y/n):\n> ").lower()
                                   if again.lower().strip() != "y":
                                                 break
                            
                                   print("Completed!\n")
                                   break

                     elif choice.lower().strip() in ("stopwatch", "sw"):
                                   exit_program = False
                                   print("\nCommands: start | stop | reset | quit")

                                   # start stopwatch thread
                                   thread = threading.Thread(target=stopwatch, daemon=True)
                                   thread.start()

                                   # main input loop
                                   while True:
                                          command = input("\n> ").strip().lower()

                                          if command == "start":
                                                 if not running:
                                                        running = True
                                                        print("Started.")
                                                 else:
                                                        print("Already running.")

                                          elif command == "stop":
                                                 if not running:
                                                        print("The stopwatch has not started.")
                                                 else:
                                                        running = False
                                                        print(f"Stopped at {elapsed} seconds. ")

                                          elif command == "reset":
                                                 if running:
                                                        print("Stop before resetting.")
                                                 else:
                                                        elapsed = 0
                                                        print("Reset.")

                                          elif command == "quit":
                                                 exit_program = True
                                                 running = False
                                                 thread.join()
                                                 break

                                          else:
                                                 print("Unknown command.")
                     
                     elif choice.lower().strip() in ("calculator", "calc"):
                            while True:
                                   try:
                                          num1 = float(input("Please enter your first number:\n> "))
                                          num2 = float(input("Please enter your second number:\n> "))
                                   except ValueError:
                                          print("Numbers only. Try again.")
                                          continue

                                   while True:
                                          operation = input("Please enter your operation (+, -, *, /) or 'q' to quit:\n> ")
                                          if operation.strip() == "+":
                                                 print("Your answer is", num1 + num2)
                                                 calculated = True
                                                 break
                                          elif operation.strip() == "-":
                                                 print("Your answer is", num1 - num2)
                                                 calculated = True
                                                 break
                                          elif operation.strip() == "*":
                                                 print("Your answer is", num1 * num2)
                                                 calculated = True
                                                 break
                                          elif operation.strip() == "/":
                                                 if num2 == 0:
                                                        print("You can't divide by zero.")
                                                 else:
                                                        print("Your answer is", num1 / num2)
                                                        calculated = True
                                                        break
                                          elif operation.strip().lower() == "q":
                                                 calc = False
                                                 break
                                          else:
                                                 print("Invalid operation.")
                                                 continue
                                   again = input("Do this again? (y/n): ").lower()
                                   if again.strip().lower() != "y":
                                          break
                     elif choice.lower().strip() in ("tally counter", "tly"):
                            count = 0
                            while True:
                                   tc_value = input("Hit enter to increase the count by 1. To end the counter, type 'stop'.")
                                   if tc_value.strip().lower() == "stop":
                                          break
                                   count = count + 1
                                   print(f"The count is currently at {count}.")
                                   continue
                            again = input("Do this again? (y/n):\n> ").lower()
                            if again.lower().strip() == "y":
                                   continue
                            else:
                                   pass
                     elif choice.lower().strip() in ("system stats", "sys"):
                            while True:
                                   monitor_running = True
                                   print("\nType 'stop' to exit the system monitor.\n")

                                   thread = threading.Thread(target=system_monitor, daemon=True)
                                   thread.start()

                                   while True:
                                          sys_cmd = input("> ").strip().lower()

                                          if sys_cmd == "stop":
                                                 monitor_running = False
                                                 thread.join()
                                                 print("\nSystem monitor stopped.")
                                                 break
                                          else:
                                                 print("Unknown command. Type 'stop' to exit.")

                                   again = input("Do this again? (y/n):\n> ").strip().lower()
                                   if again != "y":
                                          break
                     directoryReturn = input("Run the directory again? (y/n):\n> ")
                     if directoryReturn.strip().lower() in ("y", "yes"):
                            continue
                     else:
                            print("Thanks for using the app! To report any bugs, join the Discord or report an issue on GitHub.")
                            break

except (KeyboardInterrupt, EOFError):
       print(break_msg)
       exit_program = True
       running = False
       calc = False
       sys.exit()