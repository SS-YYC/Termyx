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
    try:
        while True:
            print("\033]0;Termyx - Coin Flipper\007", end="", flush=True)
            print(f"{YELLOW}Heads or tails?{RESET}")
            print(f"Enter {YELLOW}'quit (q)'{RESET} to quit.")
            command = input("Press Enter to flip the coin.\n\n> ").strip().lower()
            if command in ("quit", "q", "stop", "s"):
                break
            spin(2)
            result = random.choice(["Heads", "Tails"])
            print(f"{GREEN}{result}!{RESET}")
    except (KeyboardInterrupt, EOFError):
        print(f"\n{YELLOW}Coin Flipper interrupted.{RESET}")
