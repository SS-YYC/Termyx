import time
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET

try:
    import winsound
except ImportError:
    winsound = None


def _beep():
    for _ in range(5):
        if winsound is not None:
            try:
                winsound.Beep(1000, 300)
            except RuntimeError:
                print("\a", end="", flush=True)
        else:
            print("\a", end="", flush=True)
        time.sleep(1)


def _final_beep():
    if winsound is not None:
        try:
            for _ in range(3):
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                time.sleep(1)
            return
        except RuntimeError:
            pass

    _beep()


def _countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"\r{CYAN}{int(mins):02d}:{int(secs):02d} remaining{RESET} ", end="", flush=True)
        seconds -= 1
        time.sleep(1)
    print()
    print(f"{GREEN}Completed!{RESET}")
    _final_beep()


def _interval():
    while True:
        try:
            print(f"Enter {YELLOW}'quit (q)'{RESET} to quit.")
            start_raw = input("Please enter the starting number:\n\n> ").strip()
            if start_raw.lower() in ("quit", "q", "stop", "s"):
                return
            startNumber = float(start_raw)
            end_raw = input("Please enter the end number (must be less than the starting number):\n\n> ").strip()
            if end_raw.lower() in ("quit", "q", "stop", "s"):
                return
            endNumber = float(end_raw)
            if endNumber >= startNumber:
                print(f"{RED}The end number must be less than the starting number.{RESET}")
                continue
            interval_raw = input("Please enter the interval to count down by:\n\n> ").strip()
            if interval_raw.lower() in ("quit", "q", "stop", "s"):
                return
            interval = float(interval_raw)
            if interval <= 0:
                print(f"{RED}Interval must be greater than 0.{RESET}")
                continue
            delay_raw = input("Please enter the delay between steps (secs):\n\n> ").strip()
            if delay_raw.lower() in ("quit", "q", "stop", "s"):
                return
            delay = float(delay_raw)
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
        _final_beep()
        break


def run():
    try:
        print("\033]0;Termyx - Timer\007", end="", flush=True)
        while True:
            print(f"{YELLOW}Tick tock!{RESET}")
            print(f"\n{YELLOW}Timer modes: countdown (cd/c) | interval (int/i){RESET}")
            print(f"Enter {YELLOW}'quit (q)'{RESET} to quit.")
            mode = input("\n> ").strip().lower()

            if mode in ("quit", "q", "stop", "s"):
                break

            if mode in ("countdown", "cd", "c"):
                while True:
                    print("\033]0;Termyx - Countdown Timer\007", end="", flush=True)
                    try:
                        duration_raw = input("Please enter the duration of your timer in minutes:\n\n> ").strip()
                        if duration_raw.lower() in ("quit", "q", "stop", "s"):
                            return
                        duration = float(duration_raw)
                    except ValueError:
                        print(f"{RED}Numbers only. Try again.{RESET}")
                        continue
                    if duration <= 0:
                        print(f"{RED}Please enter a positive number greater than 0.{RESET}")
                        continue
                    _countdown(duration * 60)
                    break

            elif mode in ("interval", "int", "i"):
                print("\033]0;Termyx - Interval Timer\007", end="", flush=True)
                _interval()

            else:
                print(f"{RED}Invalid mode. Please type 'countdown', 'cd', or 'c', or 'interval', 'int', or 'i'.{RESET}")
                continue

            again = input("\nSet another timer? (Y/n)\n\n> ").strip().lower()
            if again not in ("", "y", "yes"):
                break
    except (KeyboardInterrupt, EOFError):
        print(f"\n{YELLOW}Timer interrupted.{RESET}")
