import time
import threading

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
            print(f"\rElapsed: {elapsed} seconds ", end="", flush=True)
        else:
            time.sleep(0.1)


def run():
    global running, elapsed, exit_program

    running = False
    elapsed = 0
    exit_program = False

    print("\nCommands: start | stop | reset | quit")

    thread = threading.Thread(target=_stopwatch_thread, daemon=True)
    thread.start()

    while True:
        command = input("\n> ").strip().lower()

        if command == "start":
            if not running:
                running = True
                print("Started.")
            else:
                print("Already running.")

        elif command == "stop":
            if not running:
                print("The stopwatch has not started.")
            else:
                running = False
                print(f"Stopped at {elapsed} seconds.")

        elif command == "reset":
            if running:
                print("Stop before resetting.")
            else:
                elapsed = 0
                print("Reset.")

        elif command == "quit":
            exit_program = True
            running = False
            thread.join()
            break

        else:
            print("Unknown command.")
