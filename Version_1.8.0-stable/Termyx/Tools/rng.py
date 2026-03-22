import random
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET


def run():
    try:
        while True:
            print(f"{YELLOW}Welcome to the Random Number Generator!{RESET}")
            try:
                print("Note: negative numbers are allowed - just make sure the upper limit is greater than the lower limit. Whole numbers only.")
                lower = int(input("Enter the lower limit number:\n> "))
                upper = int(input("Enter the upper limit number:\n> "))
            except ValueError:
                print(f"{RED}Whole numbers only. Try again.{RESET}")
                continue

            if lower >= upper:
                print(f"{RED}The upper limit must be greater than the lower limit.{RESET}")
                continue

            print(f"{GREEN}Your random number is: {random.randint(lower, upper)}{RESET}")

            again = input("\nDo this again? (y/n):\n> ").strip().lower()
            if again not in ("y", "yes"):
                break
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Random Number Generator interrupted.{RESET}")