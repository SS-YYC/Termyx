import sys
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET


def run():
    try:
        while True:
            print("\033]0;Termyx - Tally Counter\007", end="", flush=True)
            print(f"{YELLOW}One at a time.{RESET}")
            count = 0
            print(f"Press Enter to increase the count by 1. To end the counter, type {YELLOW}'quit (q)'{RESET} and press Enter.")
            while True:
                print(f"{CYAN}The count is currently at {count}.{RESET}")
                tc_value = input("\n> ")
                if tc_value.strip().lower() in ("quit", "q", "stop", "s"):
                    print()
                    break
                count += 1
                sys.stdout.write("\033[2A")
                sys.stdout.flush()

            print(f"{GREEN}Final count: {count}{RESET}")
            again = input("\nCount again? (Y/n)\n\n> ").strip().lower()
            if again not in ("", "y", "yes"):
                break
    except (KeyboardInterrupt, EOFError):
        print(f"\n{YELLOW}Tally Counter interrupted.{RESET}")
