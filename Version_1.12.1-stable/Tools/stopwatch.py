import time
import threading
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET

running = False
elapsed = 0
exit_program = False
name = None

def _format_time(seconds):
    mins, secs = divmod(seconds, 60)
    return f"{int(mins):02d}:{int(secs):02d}"


def _stopwatch_thread():
    global elapsed, running, exit_program
    while not exit_program:
        if running:
            time.sleep(1)
            if not running:
                continue
            elapsed += 1
            print(f"\r{CYAN}Elapsed: {_format_time(elapsed)} {RESET}", end="", flush=True)
        else:
            time.sleep(0.1)


def run():
    global running, elapsed, exit_program, laps
    name = None
    running = False
    elapsed = 0
    exit_program = False
    laps = []
    print(f"{YELLOW}Ready when you are.{RESET}")
    print(f"\n{YELLOW}Commands: start (s) | stop (st) | reset (r) | lap (l) | quit (q) | name (n){RESET}")
    print(f"Type {YELLOW}'quit (q)'{RESET} to return to the directory.")
    print(f"Type {YELLOW}'name (n)'{RESET} to assign a name to this stopwatch session (for display purposes only).")
    thread = threading.Thread(target=_stopwatch_thread, daemon=True)
    thread.start()
    try:
        print("\033]0;Termyx - Stopwatch\007", end="", flush=True)
        while True:
            command = input("\n> ").strip().lower()

            if command == "start" or command == "s":
                if not running:
                    running = True
                    print(f"{GREEN}Started stopwatch '{name}'.{RESET}") if name else print(f"{GREEN}Started.{RESET}")
                else:
                    print(f"{RED}Already running.{RESET}")

            elif command == "stop" or command == "st":
                if not running:
                    print(f"{RED}The stopwatch is not running.{RESET}")
                else:
                    running = False
                    print(f"{GREEN}Stopped at {_format_time(elapsed)}.{RESET}")

            elif command == "reset" or command == "r":
                if running:
                    print(f"{RED}Stop the stopwatch before resetting it.{RESET}")
                else:
                    elapsed = 0
                    laps = []
                    print(f"\r{CYAN}Elapsed: 00:00 {RESET}", end="", flush=True)
                    print(f"\n{GREEN}Reset.{RESET}")

            elif command == "lap" or command == "l":
                if not running:
                    print(f"{RED}The stopwatch is not running.{RESET}")
                else:
                    laps.append(elapsed)
                    print(f"{GREEN}Lap {len(laps)}: {_format_time(elapsed)}{RESET}")

            elif command == "quit" or command == "q":
                exit_program = True
                running = False
                if laps:
                    print(f"\n{YELLOW}Lap times:{RESET}")
                    for i, lap in enumerate(laps, 1):
                        print(f"{CYAN}  Lap {i}: {_format_time(lap)}{RESET}")
                thread.join()
                break
            elif command == "name" or command == "n":
                name = input("Enter a name for this stopwatch session:\n\n> ").strip().capitalize()
                if name:
                    print(f"{GREEN}Stopwatch session named '{name}'.{RESET}")
                else:
                    name = None
                    print(f"{YELLOW}Name cleared.{RESET}")
            else:
                print(f"{RED}Unknown command.{RESET}")
    except (KeyboardInterrupt, EOFError):
        print(f"\n{YELLOW}Stopwatch '{name}' interrupted.{RESET}") if name else print(f"\n{YELLOW}Stopwatch interrupted.{RESET}")
        exit_program = True
        running = False
        thread.join()
