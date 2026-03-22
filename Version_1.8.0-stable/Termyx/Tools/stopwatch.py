import time
import threading
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET

running = False
elapsed = 0
exit_program = False


def _stopwatch_thread():
    global elapsed, running, exit_program
    while not exit_program:
        if running:
            time.sleep(1)
            if not running:
                continue
            elapsed += 1
            print(f"\r{CYAN}Elapsed: {elapsed} seconds {RESET}", end="", flush=True)
        else:
            time.sleep(0.1)


def run():
    global running, elapsed, exit_program

    running = False
    elapsed = 0
    exit_program = False
    print(f"{YELLOW}Welcome to the Stopwatch!{RESET}")
    print(f"\n{YELLOW}Commands: start | stop | reset | quit{RESET}")

    thread = threading.Thread(target=_stopwatch_thread, daemon=True)
    thread.start()
    try:
        while True:
            command = input("\n> ").strip().lower()

            if command == "start":
                if not running:
                    running = True
                    print(f"{GREEN}Started.{RESET}")
                else:
                    print(f"{RED}Already running.{RESET}")

            elif command == "stop":
                if not running:
                    print(f"{RED}The stopwatch has not started.{RESET}")
                else:
                    running = False
                    print(f"{GREEN}Stopped at {elapsed} seconds.{RESET}")

            elif command == "reset":
                if running:
                    print(f"{RED}Stop before resetting.{RESET}")
                else:
                    elapsed = 0
                    print(f"{GREEN}Reset.{RESET}")

            elif command == "quit":
                exit_program = True
                running = False
                thread.join()
                break

            else:
                print(f"{RED}Unknown command.{RESET}")
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Stopwatch interrupted.{RESET}")
        exit_program = True
        running = False
        thread.join()