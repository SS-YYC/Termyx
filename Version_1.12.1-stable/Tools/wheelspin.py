import random
import sys
import time
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET


def animate_wheelspin(options, result):
    spinner = ["|", "/", "-", "\\"]
    for i in range(20):
        sys.stdout.write(f"\r\033[2K{CYAN}{spinner[i % 4]} {random.choice(options)}{RESET}")
        sys.stdout.flush()
        time.sleep(0.1)

    sys.stdout.write(f"\r\033[2K{GREEN}Result: {result}{RESET}\n")
    sys.stdout.flush()


def _get_options(min_count):
    print("\nEnter options separated by commas (e.g. apple, banana, cherry).")
    print(f"Type {YELLOW}'quit (q)'{RESET} to return.")
    raw = input("\n> ").strip()
    if raw.lower() in ("", "quit", "q", "stop", "s"):
        return None

    options = [opt.strip() for opt in raw.split(",") if opt.strip()]
    if len(options) < min_count:
        if min_count == 1:
            print(f"{RED}No valid options entered.{RESET}")
        else:
            print(f"{RED}Please enter at least {min_count} valid options.{RESET}")
        return None
    return options


def random_wheel():
    print("\033]0;Termyx - Random Wheel\007", end="", flush=True)
    options = _get_options(2)
    if options is None:
        return
    result = random.choice(options)
    animate_wheelspin(options, result)


def elimination_wheel():
    print("\033]0;Termyx - Elimination Wheel\007", end="", flush=True)
    options = _get_options(2)
    if options is None:
        return

    while len(options) > 1:
        result = random.choice(options)
        animate_wheelspin(options, result)
        options.remove(result)
        proceed = input(f"Press Enter to remove the selected option and continue, or type {YELLOW}'quit (q)'{RESET} to return.\n\n> ").strip().lower()
        if proceed in ("quit", "q", "stop", "s"):
            print(f"\n{YELLOW}Wheel Spinner closed before a final pick was chosen.{RESET}")
            return

    print(f"\n{GREEN}Final pick: {options[0]}{RESET}")


def run():
    try:
        while True:
            print("\033]0;Termyx - Wheel Spinner\007", end="", flush=True)
            print(f"\n{YELLOW}Welcome to the Wheel Spinner!{RESET}")
            print("Choose a mode: random (r/rand) | elimination (e/elim)")
            print(f"Type {YELLOW}'quit (q)'{RESET} to return.")
            choice = input("\n> ").strip().lower()

            if choice in ("", "quit", "q", "stop", "s"):
                break
            elif choice in ("r", "rand", "random"):
                random_wheel()
                again = input("\nSpin again? (Y/n)\n\n> ").strip().lower()
                if again not in ("", "y", "yes"):
                    break
            elif choice in ("e", "elim", "elimination"):
                elimination_wheel()
            else:
                print(f"{RED}Invalid entry.{RESET}")
    except (KeyboardInterrupt, EOFError):
        print(f"\n{YELLOW}Wheel Spinner interrupted.{RESET}")
    except (KeyboardInterrupt, EOFError):
        print(f"\n{YELLOW}Wheel Spinner interrupted.{RESET}")
