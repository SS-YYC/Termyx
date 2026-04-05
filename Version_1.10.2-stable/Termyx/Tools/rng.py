import random
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET


def run():
    try:
        while True:
            print("\033]0;Termyx - Random Number Generator\007", end="", flush=True)
            print(f"{YELLOW}Feeling lucky-{RESET}")
            print("Note: negative numbers are allowed - just make sure the upper limit is greater than the lower limit. Whole numbers only.")
            try:
                lower = int(input("Enter the lower limit number:\n> "))
                upper = int(input("Enter the upper limit number:\n> "))
            except ValueError:
                print(f"{RED}Whole numbers only. Try again.{RESET}")
                continue

            if lower >= upper:
                print(f"{RED}The upper limit must be greater than the lower limit.{RESET}")
                continue

            print(f"{GREEN}Your random number is: {random.randint(lower, upper)}{RESET}")

            again = input("\nTry your luck again? (Y/n):\n> ").strip().lower()
            if again not in ("y", "yes"):
                break
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Random Number Generator interrupted.{RESET}")
