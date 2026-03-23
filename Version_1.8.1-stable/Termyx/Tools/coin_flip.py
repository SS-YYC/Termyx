import random
import time
import sys
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET

SPINNER = ["|", "/", "-", "\\"]


def spin(duration):
    start = time.time()
    i = 0
    while time.time() - start < duration:
        sys.stdout.write(f"\r{CYAN}{SPINNER[i % len(SPINNER)]} {RESET}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write("\r  \r")
    sys.stdout.flush()


def run():
    while True:
        try:
            print(f"{YELLOW}Welcome to the Coin Flipper!{RESET}")
            input("Press Enter to flip the coin...")
            spin(2)
            result = random.choice(["Heads", "Tails"])
            print(f"{GREEN}{result}!{RESET}")
            again = input("\nDo this again? (y/n):\n> ").strip().lower()
            if again not in ("y", "yes"):
                break
        except KeyboardInterrupt:
            print(f"\n{YELLOW}Coin Flipper interrupted.{RESET}")
            break