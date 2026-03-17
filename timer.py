import time
import datetime

def _countdown(timedFrom):
    while timedFrom > 0:
        print(f"\r{timedFrom} ", end="", flush=True)
        timedFrom -= 1
        time.sleep(1)
    print()
    print("Completed!")
    for i in range(5):
        print("\a", end="", flush=True)
        time.sleep(1)


def _interval():
    while True:
        try:
            startNumber = float(input("Please enter the starting number:\n> "))
            endNumber = float(input("Please enter the end number (must be less than the starting number):\n> "))
            if endNumber >= startNumber:
                print("The end number must be less than the starting number.")
                continue
            interval = float(input("Please enter the interval to count down by:\n> "))
            if interval <= 0:
                print("Interval must be greater than 0.")
                continue
            delay = float(input("Please enter the delay between steps (secs):\n> "))
            if delay < 0:
                print("Delay cannot be negative.")
                continue
        except ValueError:
            print("Numbers only. Try again.")
            continue

        epsilon = 1e-9
        prev = startNumber
        while startNumber + epsilon > endNumber:
            print(startNumber)
            prev = startNumber
            startNumber -= interval
            time.sleep(delay)

        # Only print end number if the last printed value didn't already land on it
        if abs(prev - endNumber) > epsilon:
            print(endNumber)

        print("Completed!")
        for i in range(5):
            print("\a", end="", flush=True)
            time.sleep(1)
        break


def run():
    while True:
        print("\nTimer modes: countdown (cd) | interval (int)")
        mode = input("> ").strip().lower()

        if mode in ("countdown", "cd"):
            while True:
                try:
                    timedFrom = int(input("Please enter the duration of your timer in seconds:\n> "))
                except ValueError:
                    print("Whole numbers only. Try again.")
                    continue
                if timedFrom <= 0:
                    print("Please enter a positive number greater than 0.")
                    continue
                _countdown(timedFrom)
                break

        elif mode in ("interval", "int"):
            _interval()

        else:
            print("Invalid mode. Please type 'countdown' or 'cd', or 'interval' or 'int'.")
            continue

        again = input("\nDo this again? (y/n):\n> ").strip().lower()
        if again not in ("y", "yes"):
            break