import sys
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET


def run():
    try:
        while True:
            print(f"{YELLOW}Welcome to the Tally Counter!{RESET}")
            count = 0
            print("Hit enter to increase the count by 1. To end the counter, type 'stop' and hit enter.")
            while True:
                print(f"{CYAN}The count is currently at {count}.{RESET}")
                tc_value = input("> ")
                if tc_value.strip().lower() == "stop":
                    print()
                    break
                count += 1
                sys.stdout.write("\033[2A")
                sys.stdout.flush()

            print(f"{GREEN}Final count: {count}{RESET}")
            again = input("\nDo this again? (y/n):\n> ").strip().lower()
            if again not in ("y", "yes"):
                break
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Tally Counter interrupted.{RESET}")