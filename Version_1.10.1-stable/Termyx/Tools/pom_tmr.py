import time
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET
from Tools.settings import load_pom_defaults

try:
    import winsound
except ImportError:
    winsound = None


def _beep():
    for _ in range(3):
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
        print(f"\r{CYAN}{int(mins):02d}:{int(secs):02d} remaining.{RESET} ", end="", flush=True)
        time.sleep(1)
        seconds -= 1
    print()


def run():
    while True:
        try:
            print("\033]0;Termyx - Pomodoro Timer\007", end="", flush=True)
            print(f"{YELLOW}Let's get to work.{RESET}")
            print("Hit Enter to use the default value for any setting. All values entered here will save for the future.\n")
            defaults = load_pom_defaults()

            while True:
                try:
                    work_duration = float(input(f"Work period duration in minutes (default: {defaults['work']}):\n> ") or defaults["work"])
                    sbrk = float(input(f"Short break duration in minutes (default: {defaults['short_break']}):\n> ") or defaults["short_break"])
                    lbrk = float(input(f"Long break duration in minutes (default: {defaults['long_break']}):\n> ") or defaults["long_break"])
                    loops = int(input(f"Number of Pomodoros to complete (default: {defaults['loops']}):\n> ") or defaults["loops"])

                    if any(v <= 0 for v in (work_duration, sbrk, lbrk, loops)):
                        print(f"{RED}All values must be greater than 0. Please try again.{RESET}")
                        continue
                    break
                except ValueError:
                    print(f"{RED}One of your inputs could not be recognized. Please try again.{RESET}")
                    continue

            print(f"\n{CYAN}Set: You'll be working for {work_duration} minutes with your short break being {sbrk} minutes long and your long break being {lbrk} minutes long. This will repeat for {loops} Pomodoros.{RESET}")
            for i in range(3, 0, -1):
                print(f"\rStarting in {i}...", end="", flush=True)
                time.sleep(1)
            print("\r                \r", end="")

            for i in range(1, loops + 1):
                print(f"{YELLOW}Pomodoro {i} of {loops} - Work session starting!{RESET}")
                _countdown(work_duration * 60)
                if i == loops:
                    _final_beep()
                else:
                    _beep()

                if i == loops:
                    print(f"{GREEN}All Pomodoros complete! Great work!{RESET}")
                    long_breaks = (loops - 1) // 4
                    short_breaks = (loops - 1) - long_breaks
                    print(f"{GREEN}You worked for a total of {loops * work_duration} minutes, and took {short_breaks} short breaks and {long_breaks} long breaks - for a total of {short_breaks * sbrk + long_breaks * lbrk} minutes of break time. Enjoy your well-earned rest!{RESET}")
                    break
                elif i % 4 == 0:
                    print(f"{YELLOW}Time for a long break! ({lbrk} minutes){RESET}")
                    _countdown(lbrk * 60)
                    _beep()
                    print(f"{GREEN}Break over - get back to work!{RESET}\n")
                else:
                    print(f"{YELLOW}Time for a short break! ({sbrk} minutes){RESET}")
                    _countdown(sbrk * 60)
                    _beep()
                    print(f"{GREEN}Break over - get back to work!{RESET}\n")

            again = input("\nAnother session? (Y/n):\n> ").lower().strip()
            if again in ("y", "yes"):
                continue
            else:
                break
        except (KeyboardInterrupt, EOFError):
            print(f"\n{YELLOW}Pomodoro Timer interrupted.{RESET}")
            break
