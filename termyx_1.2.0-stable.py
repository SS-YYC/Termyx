import time
import sys
import threading

changelog = ("""
\n
Changelog:

Added in Version 1.2.0:
             
• A new calculator function has been added.
• Rebranding to Termyx to better suit the functions now offered in the app.
• Phase 1 of a UX overhaul to allow more functionality. 

And the following bug fixes:

• Various bugs in the stopwatch have been fixed.
• Various UI improvements and bug fixes.
             
IN THE WORKS:

• Sound confirmation when the user's timer has ended
• A new GUI to interact with the app.
• A tally counter function - this shouldn't take long 👀
• Various optimization improvements.
• With the new UX logic, there are some issues with the break logic. While I have a temporary fix in place, this will be properly fixed soon enough. However, it isn't that big a deal, because the app works fine.
• Phase 2 of the UX overhaul, adding more shorthands for the directory - it's tricky to use right now. (v.1.2.1?)

""")




break_msg = "\nApp terminated successfully. Goodbye!"
running = False
run = True
elapsed = 0
exit_program = False
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
 _____                                      _   ____    ___   
|_   _|__ _ __ _ __ ___  _   ___  __ __   _/ | |___ \  / _ \  
  | |/ _ \ '__| '_ ` _ \| | | \ \/ / \ \ / / |   __) || | | | 
  | |  __/ |  | | | | | | |_| |>  <   \ V /| |_ / __/ | |_| | 
  |_|\___|_|  |_| |_| |_|\__, /_/\_\   \_(_)_(_)_____(_)___/  
 _             ____ ____ |___/_   ____   ______               
| |__  _   _  / ___/ ___|    \ \ / /\ \ / / ___|              
| '_ \| | | | \___ \___ \ ____\ V /  \ V / |                  
| |_) | |_| |  ___) |__) |_____| |    | || |___               
|_.__/ \__, | |____/____/      |_|    |_| \____|              
       |___/                                                           

Termyx - a CLI app.           
Version 1.2.0-beta                                      
              """)

print ("Welcome to Termyx - made by SS-YYC! This is your all in one multi-function CLI app that can run straight off your PC!")
print ("Please follow the instructions below to use the app! To quit at any time, hit CTRL + C on your keyboard.")

cl = input ("Hit Enter to proceed. To view the changelog, type 'changelog' or 'cl'. ")
if cl.lower().strip() in ("changelog", "cl"):
       print(changelog)
else: 
       pass

#variable declaration
directory = ("Counter", "Timer", "Stopwatch", "Calculator")
stopwatchNumber = 0

while run == True:
       try:
              #Asks the user which of the avaliable tools they'd like to use.
              while True:
                     try:
                            choice = input(f"\nPlease select the tool you'll be using today out of these options: {directory}.\n> ")
                            if choice.capitalize().strip() in directory:
                                   break
                            else:
                                   print("Invalid entry.")
                                   time.sleep(0.5)
                                   continue
                     except ValueError:
                            print("One of your inputs is not recognized by the system.")
                            continue

              if choice.capitalize().strip() == "Timer": #Timer Component
                     while True:
                            try:
                                   timedFrom = int(input("\nPlease enter the duration of your timer in seconds: \n> "))
                            except ValueError:
                                   print("One of your inputs could not be recognized! Please try again.")
                                   continue

                            if timedFrom <= 0:
                                   print("Please enter a positive number greater than 0.")
                                   continue

                            while timedFrom > 0:
                                   print(timedFrom)
                                   timedFrom -= 1
                                   time.sleep(1)

                            print("Completed!")
                            again = input("Do this again? (y/n):\n> ").lower()
                            if again != "y":
                                          break

              elif choice.capitalize().strip() == "Counter": #Counter
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
                            if again != "y":
                                          break
                     
                            print("Completed!\n")
                            break

              elif choice.capitalize().strip() == "Stopwatch":
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
              
              elif choice.capitalize().strip() == "Calculator":
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
              directoryReturn = input("Run the directory again? (y/n) ")
              if directoryReturn.strip().lower() in ("y", "yes"):
                     continue
              else:
                     print("Thanks for using the app! To report any bugs, feel free to message ss.yyc on Discord.")
                     break

       except (KeyboardInterrupt, EOFError):
              print(break_msg)
              exit_program = True
              running = False
              calc = False
              sys.exit()