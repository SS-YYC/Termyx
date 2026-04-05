from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET, THEMES, THEME_DESCRIPTIONS
from Tools.colours import set_theme, save_theme, load_theme
from Tools.config_store import load_config, save_config


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

    t = input("\n> ").strip().lower()
    if t in THEMES:
        set_theme(t)
        try:
            save_theme(t)
            print(f"{GREEN}Theme set to {t}. Restart Termyx to apply.{RESET}")
        except OSError:
            print(f"{RED}Theme was applied for this session, but could not be saved.{RESET}")
    elif t == "":
        print(f"{YELLOW}No changes made.{RESET}")
    else:
        print(f"{RED}Invalid theme.{RESET}")


def run():
    try:
        while True:
            print(f"\n{YELLOW}Settings:{RESET}")
            print(f"""
{CYAN}- Theme Selection (th){RESET}
{CYAN}- Pomodoro Defaults (pom){RESET}
""")
            choice = input("> ").strip().lower()

            if choice in ("theme", "th"):
                select_theme()
            elif choice in ("pomodoro", "pom"):
                _pomodoro_settings()
            elif choice == "":
                break
            else:
                print(f"{RED}Invalid entry.{RESET}")
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Settings interrupted.{RESET}")


def _pomodoro_settings():
    defaults = load_pom_defaults()
    print(f"\n{YELLOW}Pomodoro Defaults:{RESET}")
    print(f"Current: {defaults['work']} min work | {defaults['short_break']} min short break | {defaults['long_break']} min long break | {defaults['loops']} loops")
    print("Hit Enter to keep the current value.\n")
    try:
        work = float(input(f"Work duration (default: {defaults['work']}):\n> ") or defaults["work"])
        sbrk = float(input(f"Short break (default: {defaults['short_break']}):\n> ") or defaults["short_break"])
        lbrk = float(input(f"Long break (default: {defaults['long_break']}):\n> ") or defaults["long_break"])
        loops = int(input(f"Pomodoros (default: {defaults['loops']}):\n> ") or defaults["loops"])

        if any(v <= 0 for v in (work, sbrk, lbrk, loops)):
            print(f"{RED}All values must be greater than 0. Settings not saved.{RESET}")
            return

        save_pom_defaults(work, sbrk, lbrk, loops)
        print(f"{GREEN}Pomodoro defaults saved.{RESET}")
    except ValueError:
        print(f"{RED}Invalid input. Settings not saved.{RESET}")
