from datetime import datetime
import time
import threading
import psutil
import sys

monitor_running = False


def _monitor_thread():
    global monitor_running

    psutil.cpu_percent(None)
    time.sleep(0.5)
    first = True

    while monitor_running:
        cpu = psutil.cpu_percent(None)
        ram = psutil.virtual_memory().percent
        du = psutil.disk_usage('C:/').percent
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

        sys.stdout.write(f"\033[2K{now}\n")
        sys.stdout.write(f"\033[2KCPU: {cpu}% | RAM: {ram}% | Disk: {du}%{bat_str}\n")
        sys.stdout.write("\033[2K\n")
        sys.stdout.flush()

        first = False
        time.sleep(0.5)


def run():
    global monitor_running
    try:
        while True:
            monitor_running = True
            print("Starting system monitor...")
            print("\nType 'stop' to exit the system monitor.\n")

            thread = threading.Thread(target=_monitor_thread, daemon=True)
            thread.start()

            while True:
                sys_cmd = input("> ").strip().lower()

                if sys_cmd == "stop":
                    monitor_running = False
                    thread.join()
                    print("\nSystem monitor stopped.")
                    break
                else:
                    print("Unknown command. Type 'stop' to exit.")

            again = input("\nDo this again? (y/n):\n> ").strip().lower()
            if again not in ("y", "yes"):
                break
    except KeyboardInterrupt:
        monitor_running = False
        print("\nSystem monitor interrupted.")