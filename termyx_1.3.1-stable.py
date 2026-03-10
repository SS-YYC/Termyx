import time
import sys
import threading

changelog = ("""
\n
Changelog:

Added in Version 1.3.1:
             
• The timer function has been rescripted to have a more consistent UX to the rest of the app.
• Sound output when the timer ends has been added.

And the following bug fixes:
• The 'Do this again?' logic has been fixed to account for typing errors.
• Various UI changes
             
In the Works:
• A new GUI to interact with the app.
• A new 'help' command to view helplinks and a slimmed UX guide.
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
#beginning credits/intro

print(r"""
 _____                                      _   _____  _ 
|_   _|__ _ __ _ __ ___  _   ___  __ __   _/ | |___ / / |
  | |/ _ \ '__| '_ ` _ \| | | \ \/ / \ \ / / |   |_ \ | |
  | |  __/ |  | | | | | | |_| |>  <   \ V /| |_ ___) || |
  |_|\___|_|  |_| |_| |_|\__, /_/\_\   \_(_)_(_)____(_)_|
 _             ____ ____ |___/_   ____   ______          
| |__  _   _  / ___/ ___|    \ \ / /\ \ / / ___|         
| '_ \| | | | \___ \___ \ ____\ V /  \ V / |             
| |_) | |_| |  ___) |__) |_____| |    | || |___          
|_.__/ \__, | |____/____/      |_|    |_| \____|         
       |___/                                                                                                               
Termyx - a CLI app.           
Version 1.3.1                                     
              """)

print ("Welcome to Termyx - made by SS-YYC!")
print ("Please follow the instructions below to use the app! To quit at any time, hit CTRL + C on your keyboard.")
print (helplinks)

cl = input ("Hit Enter to proceed. To view the changelog, type 'changelog' or 'cl'. ")
if cl.lower().strip() in ("changelog", "cl"):
       print(changelog)
else: 
       pass

#variable declaration
directory_disp = ("counter (ctr)", "timer (tmr)", "stopwatch (sw)", "calculator (calc)", "tally counter (tly)")
valid_commands = (
    "counter", "ctr",
    "timer", "tmr",
    "stopwatch", "sw",
    "calculator", "calc",
    "tally counter", "tly"
)
while run == True:
       try:
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