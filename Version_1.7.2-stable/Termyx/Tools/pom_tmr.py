import time


def _beep():
    for _ in range(5):
        print("\a", end="", flush=True)
        time.sleep(1)


def _countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"\r{int(mins):02d}:{int(secs):02d} remaining. ", end="", flush=True)
        time.sleep(1)
        seconds -= 1
    print()

def run():
    while True:
        try:
            print("Welcome to the Pomodoro Timer!")
            print("Hit Enter to use the default value for any setting.\n")

            while True:
                try:
                    work_duration = float(input("Work period duration in minutes (default: 25):\n> ") or 25)
                    sbrk = float(input("Short break duration in minutes (default: 5):\n> ") or 5)
                    lbrk = float(input("Long break duration in minutes (default: 15):\n> ") or 15)
                    loops = int(input("Number of Pomodoros to complete (default: 4):\n> ") or 4)

                    if any(v <= 0 for v in (work_duration, sbrk, lbrk, loops)):
                        print("All values must be greater than 0. Please try again.")
                        continue
                    break
                except ValueError:
                    print("One of your inputs could not be recognized. Please try again.")
                    continue

            print(f"\nSet: {work_duration} min work | {sbrk} min short break | {lbrk} min long break | {loops} Pomodoros")
            print("Starting in 3 seconds...\n")
            time.sleep(3)

            for i in range(1, loops + 1):
                print(f"Pomodoro {i} of {loops} — Work session starting!")
                _countdown(work_duration * 60)
                _beep()

                if i == loops:
                    print("All Pomodoros complete! Great work!")
                    break
                elif i % 4 == 0:
                    print(f"Time for a long break! ({lbrk} minutes)")
                    _countdown(lbrk * 60)
                    _beep()
                    print("Break over — get back to work!\n")
                else:
                    print(f"Time for a short break! ({sbrk} minutes)")
                    _countdown(sbrk * 60)
                    _beep()
                    print("Break over — get back to work!\n")

            again = input("\nDo this again? (y/n):\n> ").lower().strip()
            if again in ("y", "yes"):
                continue
            else:
                break
        except KeyboardInterrupt:
            print("\nPomodoro Timer interrupted.")
            break