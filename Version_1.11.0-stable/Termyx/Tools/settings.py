from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET, THEMES, THEME_DESCRIPTIONS
from Tools.colours import set_theme, save_theme, load_theme
from Tools.config_store import load_config, save_config


class SettingsCancelled(Exception):
    pass


def load_pom_defaults():
    return load_config().get("pomodoro", {
        "work": 25,
        "short_break": 5,
        "long_break": 15,
        "loops": 4
    })


def save_pom_defaults(work, sbrk, lbrk, loops):
    data = load_config()
    data["pomodoro"] = {
        "work": work,
        "short_break": sbrk,
        "long_break": lbrk,
        "loops": loops
    }
    try:
        save_config(data)
    except OSError:
        print(f"{RED}Could not save settings.{RESET}")


def load_time_format():
    time_format = load_config().get("time_format", "12")
    if str(time_format) in ("12", "24"):
        return str(time_format)
    return "12"


def save_time_format(time_format):
    data = load_config()
    data["time_format"] = str(time_format)
    try:
        save_config(data)
    except OSError:
        print(f"{RED}Could not save settings.{RESET}")


def format_clock_time(dt):
    if load_time_format() == "24":
        return dt.strftime("%H:%M")
    return dt.strftime("%I:%M %p").lstrip("0")


def format_timestamp(dt):
    if load_time_format() == "24":
        return dt.strftime("%d/%m/%Y %H:%M:%S")
    return dt.strftime("%d/%m/%Y %I:%M:%S %p")


def select_theme():
    current = load_theme()
    print(f"\n{YELLOW}Current theme: {current}{RESET}")
    print(f"\n{YELLOW}Available themes:{RESET}")
    for name, desc in THEME_DESCRIPTIONS.items():
        marker = f"{GREEN}*{RESET} " if name == current else "  "
        theme_colour = THEMES[name]["primary"]
        print(f"{marker}{theme_colour}{name}{RESET} - {desc}")

    print(f"\n{YELLOW}Colour roles in the current theme:{RESET}")
    print(f"{YELLOW}  Primary  - headers, welcome messages, navigation hints{RESET}")
    print(f"{GREEN}  Success  - successful results and positive outcomes{RESET}")
    print(f"{RED}  Error    - errors and invalid input{RESET}")
    print(f"{CYAN}  Accent   - live values and active displays{RESET}")
    print(f"\n{GREEN}* = current theme{RESET}")
    print(f"Type {YELLOW}'quit (q)'{RESET} to return without changing the theme.")

    t = input("\n> ").strip().lower()
    if t in ("quit", "q", "stop", "s", ""):
        print(f"{YELLOW}No changes made.{RESET}")
        return
    if t in THEMES:
        set_theme(t)
        try:
            save_theme(t)
            print(f"{GREEN}Theme set to {t}. Restart Termyx to apply.{RESET}")
        except OSError:
            print(f"{RED}Theme was applied for this session, but could not be saved.{RESET}")
    else:
        print(f"{RED}Invalid theme.{RESET}")


def run():
    try:
        while True:
            print(f"\n{YELLOW}Settings:{RESET}")
            print(f"""
{CYAN}- Theme Selection (th){RESET}
{CYAN}- Pomodoro Defaults (pom){RESET}
{CYAN}- Time Format (tf){RESET}
""")
            print(f"Type {YELLOW}'quit (q)'{RESET} to return.")
            choice = input("\n> ").strip().lower()

            if choice in ("theme", "th"):
                select_theme()
            elif choice in ("pomodoro", "pom"):
                _pomodoro_settings()
            elif choice in ("time format", "tf"):
                _time_format_settings()
            elif choice in ("", "quit", "q", "stop", "s"):
                break
            else:
                print(f"{RED}Invalid entry.{RESET}")
    except (KeyboardInterrupt, EOFError):
        print(f"\n{YELLOW}Settings interrupted.{RESET}")


def _pomodoro_settings():
    defaults = load_pom_defaults()
    print(f"\n{YELLOW}Pomodoro Defaults:{RESET}")
    print(f"Current: {defaults['work']} min work | {defaults['short_break']} min short break | {defaults['long_break']} min long break | {defaults['loops']} loops")
    print("Press Enter to keep the current value.\n")
    try:
        print(f"Type {YELLOW}'quit (q)'{RESET} to return without saving.\n")
        work = _prompt_setting_value(f"Work duration (default: {defaults['work']}):", defaults["work"], float)
        sbrk = _prompt_setting_value(f"Short break (default: {defaults['short_break']}):", defaults["short_break"], float)
        lbrk = _prompt_setting_value(f"Long break (default: {defaults['long_break']}):", defaults["long_break"], float)
        loops = _prompt_setting_value(f"Pomodoros (default: {defaults['loops']}):", defaults["loops"], int)

        if any(v <= 0 for v in (work, sbrk, lbrk, loops)):
            print(f"{RED}All values must be greater than 0. Settings not saved.{RESET}")
            return

        save_pom_defaults(work, sbrk, lbrk, loops)
        print(f"{GREEN}Pomodoro defaults saved.{RESET}")
    except SettingsCancelled:
        print(f"{YELLOW}No changes made.{RESET}")
    except ValueError:
        print(f"{RED}Invalid input. Settings not saved.{RESET}")
    except EOFError:
        print(f"\n{YELLOW}Settings interrupted.{RESET}")


def _prompt_setting_value(label, default, caster):
    raw = input(f"{label}\n\n> ").strip()
    if raw == "":
        return default
    if raw.lower() in ("quit", "q", "stop", "s"):
        raise SettingsCancelled
    return caster(raw)


def _time_format_settings():
    current = load_time_format()
    print(f"\n{YELLOW}Time Format:{RESET}")
    print(f"Current: {current}-hour")
    print("Choose 12 or 24.")
    print(f"Type {YELLOW}'quit (q)'{RESET} to return without saving.")
    choice = input("\n> ").strip().lower()

    if choice in ("", "quit", "q", "stop", "s"):
        print(f"{YELLOW}No changes made.{RESET}")
        return

    if choice in ("12", "12-hour", "12 hour"):
        save_time_format("12")
        print(f"{GREEN}Time format set to 12-hour.{RESET}")
    elif choice in ("24", "24-hour", "24 hour"):
        save_time_format("24")
        print(f"{GREEN}Time format set to 24-hour.{RESET}")
    else:
        print(f"{RED}Invalid time format.{RESET}")
