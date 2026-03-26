import time
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET


def _countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"\r{CYAN}{int(mins):02d}:{int(secs):02d} remaining{RESET} ", end="", flush=True)
        seconds -= 1
        time.sleep(1)
    print()
    print(f"{GREEN}Completed!{RESET}")
    for i in range(5):
        print("\a", end="", flush=True)
        time.sleep(1)


def _interval():
    while True:
        try:
            startNumber = float(input("Please enter the starting number:\n> "))
            endNumber = float(input("Please enter the end number (must be less than the starting number):\n> "))
            if endNumber >= startNumber:
                print(f"{RED}The end number must be less than the starting number.{RESET}")
                continue
            interval = float(input("Please enter the interval to count down by:\n> "))
            if interval <= 0:
                print(f"{RED}Interval must be greater than 0.{RESET}")
                continue
            delay = float(input("Please enter the delay between steps (secs):\n> "))
            if delay < 0:
                print(f"{RED}Delay cannot be negative.{RESET}")
                continue
        except ValueError:
            print(f"{RED}Numbers only. Try again.{RESET}")
            continue

        epsilon = 1e-9
        prev = startNumber
        while startNumber + epsilon > endNumber:
            print(f"{CYAN}{startNumber}{RESET}")
            prev = startNumber
            startNumber -= interval
            time.sleep(delay)

        if abs(prev - endNumber) > epsilon:
            print(f"{CYAN}{endNumber}{RESET}")

        print(f"{GREEN}Completed!{RESET}")
        for i in range(5):
            print("\a", end="", flush=True)
            time.sleep(1)
        break


def run():
    try:
        while True:
            print(f"{YELLOW}Tick tock!{RESET}")
            print(f"\n{YELLOW}Timer modes: countdown (cd) | interval (int){RESET}")
            mode = input("> ").strip().lower()

            if mode in ("countdown", "cd"):
                while True:
                    try:
                        duration = float(input("Please enter the duration of your timer in minutes:\n> "))
                    except ValueError:
                        print(f"{RED}Numbers only. Try again.{RESET}")
                        continue
                    if duration <= 0:
                        print(f"{RED}Please enter a positive number greater than 0.{RESET}")
                        continue
                    _countdown(duration * 60)
                    break

            elif mode in ("interval", "int"):
                _interval()

            else:
                print(f"{RED}Invalid mode. Please type 'countdown' or 'cd', or 'interval' or 'int'.{RESET}")
                continue

            again = input("\nSet another timer? (y/n):\n> ").strip().lower()
            if again not in ("y", "yes"):
                break
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Timer interrupted.{RESET}")