import random
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET


def run():
    try:
        while True:
            print("\033]0;Termyx - Random Number Generator\007", end="", flush=True)
            print(f"{YELLOW}Feeling lucky?{RESET}")
            print("Note: negative numbers are allowed. Just make sure the upper limit is greater than the lower limit. Whole numbers only.")
            print(f"Enter {YELLOW}'quit (q)'{RESET} to quit.")
            try:
                lower_raw = input("Enter the lower limit number:\n\n> ").strip()
                if lower_raw.lower() in ("quit", "q", "stop", "s"):
                    break
                lower = int(lower_raw)
                upper_raw = input("Enter the upper limit number:\n\n> ").strip()
                if upper_raw.lower() in ("quit", "q", "stop", "s"):
                    break
                upper = int(upper_raw)
            except ValueError:
                print(f"{RED}Whole numbers only. Try again.{RESET}")
                continue

            if lower >= upper:
                print(f"{RED}The upper limit must be greater than the lower limit.{RESET}")
                continue

            print(f"{GREEN}Your random number is: {random.randint(lower, upper)}{RESET}")
    except (KeyboardInterrupt, EOFError):
        print(f"\n{YELLOW}Random Number Generator interrupted.{RESET}")
