from datetime import datetime
import time
import threading
import sys
import os
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET
from Tools.settings import format_timestamp

try:
    import psutil
except ImportError:
    psutil = None


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
        now = format_timestamp(datetime.now())

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
    if psutil is None:
        print(f"{RED}The System Monitor is unavailable because psutil is not installed.{RESET}")
        print(f"Run {CYAN}pip install psutil{RESET} to enable it.")
        return
    try:
        print("\033]0;Termyx - System Monitor\007", end="", flush=True)
        while True:
            monitor_running = True
            print(f"{YELLOW}Starting system monitor...{RESET}")
            print(f"\nType {YELLOW}'quit (q)'{RESET} to return to the directory.\n")

            thread = threading.Thread(target=_monitor_thread, daemon=True)
            thread.start()

            while True:
                sys_cmd = input("\n> ").strip().lower()

                if sys_cmd in ("stop", "s", "q", "quit"):
                    monitor_running = False
                    thread.join()
                    print(f"\n{GREEN}System monitor stopped.{RESET}")
                    break
                else:
                    print(f"{RED}Unknown command. Type {YELLOW}'quit (q)'{RED} to return.{RESET}")

            again = input("\nRun the system monitor again? (Y/n)\n\n> ").strip().lower()
            if again not in ("", "y", "yes"):
                break
    except (KeyboardInterrupt, EOFError):
        monitor_running = False
        print(f"\n{YELLOW}System monitor interrupted.{RESET}")
