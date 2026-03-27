from datetime import datetime
import time
import threading
import psutil
import sys
import os
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET

monitor_running = False
DISK_PATH = os.path.abspath(os.sep)
if os.name == "nt":
    DISK_PATH = os.path.splitdrive(os.path.abspath(__file__))[0] + "\\"


def _monitor_thread():
    global monitor_running

    psutil.cpu_percent(None)
    time.sleep(0.5)
    first = True

    while monitor_running:
        cpu = psutil.cpu_percent(None)
        ram = psutil.virtual_memory().percent
        du = psutil.disk_usage(DISK_PATH).percent
        battery = psutil.sensors_battery()
        now = datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")

        if battery is not None:
            plugged = "+" if battery.power_plugged else "-"
            bat_str = f" | Battery: {battery.percent}% {plugged}"
        else:
            bat_str = ""

        if not first:
            sys.stdout.write("\033[3A")
            sys.stdout.flush()

        sys.stdout.write(f"\033[2K{CYAN}{now}{RESET}\n")
        sys.stdout.write(f"\033[2K{GREEN}CPU: {cpu}% | RAM: {ram}% | Disk: {du}%{bat_str}{RESET}\n")
        sys.stdout.write("\033[2K\n")
        sys.stdout.flush()

        first = False
        time.sleep(0.25)


def run():
    global monitor_running
    try:
        while True:
            monitor_running = True
            print(f"{YELLOW}Starting system monitor...{RESET}")
            print(f"\nType {YELLOW}'quit (q)'{RESET} to exit the system monitor.\n")

            thread = threading.Thread(target=_monitor_thread, daemon=True)
            thread.start()

            while True:
                sys_cmd = input("> ").strip().lower()

                if sys_cmd == "quit" or sys_cmd == "q":
                    monitor_running = False
                    thread.join()
                    print(f"\n{GREEN}System monitor stopped.{RESET}")
                    break
                else:
                    print(f"{RED}Unknown command. Type 'quit (q)' to exit.{RESET}")

            again = input("\nRun the system monitor again? (y/n):\n> ").strip().lower()
            if again not in ("y", "yes"):
                break
    except KeyboardInterrupt:
        monitor_running = False
        print(f"\n{YELLOW}System monitor interrupted.{RESET}")
