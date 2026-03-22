import time
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET


def _beep():
    for _ in range(5):
        print("\a", end="", flush=True)
        time.sleep(1)


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
            print(f"{YELLOW}Welcome to the Pomodoro Timer!{RESET}")
            print("Hit Enter to use the default value for any setting.\n")

            while True:
                try:
                    work_duration = float(input("Work period duration in minutes (default: 25):\n> ") or 25)
                    sbrk = float(input("Short break duration in minutes (default: 5):\n> ") or 5)
                    lbrk = float(input("Long break duration in minutes (default: 15):\n> ") or 15)
                    loops = int(input("Number of Pomodoros to complete (default: 4):\n> ") or 4)

                    if any(v <= 0 for v in (work_duration, sbrk, lbrk, loops)):
                        print(f"{RED}All values must be greater than 0. Please try again.{RESET}")
                        continue
                    break
                except ValueError:
                    print(f"{RED}One of your inputs could not be recognized. Please try again.{RESET}")
                    continue

            print(f"\n{CYAN}Set: {work_duration} min work | {sbrk} min short break | {lbrk} min long break | {loops} Pomodoros{RESET}")
            for i in range(3, 0, -1):
                print(f"\rStarting in {i}...", end="", flush=True)
                time.sleep(1)
            print("\r                \r", end="")

            for i in range(1, loops + 1):
                print(f"{YELLOW}Pomodoro {i} of {loops} — Work session starting!{RESET}")
                _countdown(work_duration * 60)
                _beep()

                if i == loops:
                    print(f"{GREEN}All Pomodoros complete! Great work!{RESET}")
                    print(f"{GREEN}You worked for a total of {loops * work_duration} minutes, and took {loops - 1} short breaks and {loops // 4} long breaks - for a total of {(loops - 1) * sbrk + (loops // 4) * lbrk} minutes of break time. Enjoy your well-earned rest!{RESET}")
                    break
                elif i % 4 == 0:
                    print(f"{YELLOW}Time for a long break! ({lbrk} minutes){RESET}")
                    _countdown(lbrk * 60)
                    _beep()
                    print(f"{GREEN}Break over — get back to work!{RESET}\n")
                else:
                    print(f"{YELLOW}Time for a short break! ({sbrk} minutes){RESET}")
                    _countdown(sbrk * 60)
                    _beep()
                    print(f"{GREEN}Break over — get back to work!{RESET}\n")

            again = input("\nDo this again? (y/n):\n> ").lower().strip()
            if again in ("y", "yes"):
                continue
            else:
                break
        except (KeyboardInterrupt, EOFError):
            print(f"\n{YELLOW}Pomodoro Timer interrupted.{RESET}")
            break