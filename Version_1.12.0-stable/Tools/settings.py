import json
import os

from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET, THEMES, THEME_DESCRIPTIONS
from Tools.colours import set_theme, save_theme, load_theme
from Tools.config_store import load_config, save_config, get_config_path


class SettingsCancelled(Exception):
    pass


DIRECTORY_TOOL_OPTIONS = [
    ("stopwatch", "Stopwatch (sw)"),
    ("timer", "Timer (tmr)"),
    ("calculator", "Calculator (calc)"),
    ("tally", "Tally Counter (tly)"),
    ("system_monitor", "System Monitor (sys)"),
    ("rng", "Random Number Generator (rng)"),
    ("dice", "Dice Roller (dice)"),
    ("wheel", "Wheel Spinner (wh)"),
    ("unit_converter", "Unit Converter (uc)"),
    ("pomodoro", "Pomodoro Timer (pom)"),
    ("coin_flip", "Coin Flipper (coin)"),
    ("password_generator", "Password Generator (pwd)"),
]
DIRECTORY_TOOL_IDS = [tool_id for tool_id, _ in DIRECTORY_TOOL_OPTIONS]
DEFAULT_DIRECTORY_ORDER = DIRECTORY_TOOL_IDS[:]


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


def load_startup_behaviour():
    behaviour = load_config().get("startup_behaviour", "splash")
    if behaviour in ("splash", "skip_splash"):
        return behaviour
    return "splash"


def save_startup_behaviour(behaviour):
    data = load_config()
    data["startup_behaviour"] = behaviour
    try:
        save_config(data)
    except OSError:
        print(f"{RED}Could not save settings.{RESET}")


def load_directory_preferences():
    data = load_config()
    directory = data.get("directory", {})
    if not isinstance(directory, dict):
        directory = {}

    order = directory.get("order", DEFAULT_DIRECTORY_ORDER)
    if not isinstance(order, list):
        order = DEFAULT_DIRECTORY_ORDER
    order = [item for item in order if item in DIRECTORY_TOOL_IDS]
    for item in DEFAULT_DIRECTORY_ORDER:
        if item not in order:
            order.append(item)

    hidden = directory.get("hidden", [])
    if not isinstance(hidden, list):
        hidden = []
    hidden = [item for item in hidden if item in DIRECTORY_TOOL_IDS]

    return {"order": order, "hidden": hidden}


def save_directory_preferences(order, hidden):
    clean_order = [item for item in order if item in DIRECTORY_TOOL_IDS]
    for item in DEFAULT_DIRECTORY_ORDER:
        if item not in clean_order:
            clean_order.append(item)
    clean_hidden = [item for item in hidden if item in DIRECTORY_TOOL_IDS]

    data = load_config()
    data["directory"] = {
        "order": clean_order,
        "hidden": clean_hidden,
    }
    try:
        save_config(data)
    except OSError:
        print(f"{RED}Could not save settings.{RESET}")


def get_directory_lines(psutil_available):
    labels = dict(DIRECTORY_TOOL_OPTIONS)
    prefs = load_directory_preferences()
    lines = []

    for tool_id in prefs["order"]:
        if tool_id in prefs["hidden"]:
            continue
        if tool_id == "system_monitor":
            line = f"{CYAN}- System Monitor (sys){RESET}" if psutil_available else f"{CYAN}- System Monitor (sys) {RED}(unavailable){RESET}"
        else:
            line = f"{CYAN}- {labels[tool_id]}{RESET}"
        lines.append(line)

    return lines


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
            print(f"{RED}Theme could not be saved. Restart Termyx after saving a theme successfully to apply it app-wide.{RESET}")
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
{CYAN}- Startup Behaviour (sb){RESET}
{CYAN}- Directory Layout (dir){RESET}
{CYAN}- View Saved Config (view){RESET}
{CYAN}- Reset Config (reset){RESET}
{CYAN}- Export Config Preset (export){RESET}
{CYAN}- Import Config Preset (import){RESET}
""")
            print(f"Type {YELLOW}'quit (q)'{RESET} to return.")
            choice = input("\n> ").strip().lower()

            if choice in ("theme", "th"):
                select_theme()
            elif choice in ("pomodoro", "pom"):
                _pomodoro_settings()
            elif choice in ("time format", "tf"):
                _time_format_settings()
            elif choice in ("startup behaviour", "startup behavior", "startup", "sb"):
                _startup_behaviour_settings()
            elif choice in ("directory layout", "directory", "dir"):
                _directory_layout_settings()
            elif choice in ("view saved config", "view config", "config viewer", "view"):
                _view_saved_config()
            elif choice in ("reset config", "reset"):
                _reset_config()
            elif choice in ("export config preset", "export config", "export"):
                _export_config()
            elif choice in ("import config preset", "import config", "import"):
                _import_config()
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
        print(f"{RED}Invalid entry.{RESET}")
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


def _startup_behaviour_settings():
    current = load_startup_behaviour()
    current_label = "Skip splash and go straight to the directory" if current == "skip_splash" else "Show splash screen"
    print(f"\n{YELLOW}Startup Behaviour:{RESET}")
    print(f"Current: {current_label}")
    print(f"{CYAN}1.{RESET} Show splash screen")
    print(f"{CYAN}2.{RESET} Skip splash and go straight to the directory")
    print(f"Type {YELLOW}'quit (q)'{RESET} to return without saving.")
    choice = input("\n> ").strip().lower()

    if choice in ("", "quit", "q", "stop", "s"):
        print(f"{YELLOW}No changes made.{RESET}")
        return

    if choice in ("1", "show splash", "splash", "show splash screen"):
        save_startup_behaviour("splash")
        print(f"{GREEN}Startup behaviour set to show the splash screen.{RESET}")
    elif choice in ("2", "skip splash", "skip", "directory", "skip splash and go straight to the directory"):
        save_startup_behaviour("skip_splash")
        print(f"{GREEN}Startup behaviour set to skip the splash screen.{RESET}")
    else:
        print(f"{RED}Invalid entry.{RESET}")


def _directory_layout_settings():
    while True:
        prefs = load_directory_preferences()
        labels = dict(DIRECTORY_TOOL_OPTIONS)
        visible = [tool_id for tool_id in prefs["order"] if tool_id not in prefs["hidden"]]
        hidden = [tool_id for tool_id in prefs["order"] if tool_id in prefs["hidden"]]

        print(f"\n{YELLOW}Directory Layout:{RESET}")
        print("Current visible order:")
        if visible:
            for index, tool_id in enumerate(visible, 1):
                print(f"{CYAN}{index}.{RESET} {labels[tool_id]}")
        else:
            print(f"{RED}No tools are currently visible in the directory.{RESET}")
        print(f"\nHidden tools: {', '.join(labels[tool_id] for tool_id in hidden) if hidden else 'None'}")
        print(f"\n{CYAN}1.{RESET} Reorder visible tools")
        print(f"{CYAN}2.{RESET} Hide a tool")
        print(f"{CYAN}3.{RESET} Show a hidden tool")
        print(f"{CYAN}4.{RESET} Restore default order and visibility")
        print(f"Type {YELLOW}'quit (q)'{RESET} to return.")
        choice = input("\n> ").strip().lower()

        if choice in ("", "quit", "q", "stop", "s"):
            break
        if choice == "1":
            _reorder_directory_tools(prefs)
        elif choice == "2":
            _hide_directory_tool(prefs)
        elif choice == "3":
            _show_directory_tool(prefs)
        elif choice == "4":
            save_directory_preferences(DEFAULT_DIRECTORY_ORDER, [])
            print(f"{GREEN}Directory layout reset to defaults.{RESET}")
        else:
            print(f"{RED}Invalid entry.{RESET}")


def _reorder_directory_tools(prefs):
    labels = dict(DIRECTORY_TOOL_OPTIONS)
    visible = [tool_id for tool_id in prefs["order"] if tool_id not in prefs["hidden"]]
    if len(visible) < 2:
        print(f"{YELLOW}At least two visible tools are needed to reorder the directory.{RESET}")
        return

    print("\nEnter a new visible order using numbers separated by commas.")
    for index, tool_id in enumerate(visible, 1):
        print(f"{CYAN}{index}.{RESET} {labels[tool_id]}")
    print(f"Example: {CYAN}3,1,2{RESET}")
    print(f"Type {YELLOW}'quit (q)'{RESET} to cancel.")
    raw = input("\n> ").strip().lower()

    if raw in ("", "quit", "q", "stop", "s"):
        print(f"{YELLOW}No changes made.{RESET}")
        return

    try:
        indexes = [int(part.strip()) for part in raw.split(",")]
    except ValueError:
        print(f"{RED}Invalid entry.{RESET}")
        return

    if sorted(indexes) != list(range(1, len(visible) + 1)):
        print(f"{RED}Please enter each visible tool number exactly once.{RESET}")
        return

    new_visible = [visible[index - 1] for index in indexes]
    hidden = [tool_id for tool_id in prefs["order"] if tool_id in prefs["hidden"]]
    save_directory_preferences(new_visible + hidden, hidden)
    print(f"{GREEN}Directory order updated.{RESET}")


def _hide_directory_tool(prefs):
    labels = dict(DIRECTORY_TOOL_OPTIONS)
    visible = [tool_id for tool_id in prefs["order"] if tool_id not in prefs["hidden"]]
    if len(visible) <= 1:
        print(f"{YELLOW}At least one tool must stay visible in the directory.{RESET}")
        return

    print("\nChoose a tool number to hide:")
    for index, tool_id in enumerate(visible, 1):
        print(f"{CYAN}{index}.{RESET} {labels[tool_id]}")
    print(f"Type {YELLOW}'quit (q)'{RESET} to cancel.")
    raw = input("\n> ").strip().lower()

    if raw in ("", "quit", "q", "stop", "s"):
        print(f"{YELLOW}No changes made.{RESET}")
        return

    try:
        index = int(raw)
    except ValueError:
        print(f"{RED}Invalid entry.{RESET}")
        return

    if not 1 <= index <= len(visible):
        print(f"{RED}Invalid entry.{RESET}")
        return

    tool_id = visible[index - 1]
    save_directory_preferences(prefs["order"], prefs["hidden"] + [tool_id])
    print(f"{GREEN}{labels[tool_id]} hidden from the directory.{RESET}")


def _show_directory_tool(prefs):
    labels = dict(DIRECTORY_TOOL_OPTIONS)
    hidden = [tool_id for tool_id in prefs["order"] if tool_id in prefs["hidden"]]
    if not hidden:
        print(f"{YELLOW}No hidden tools to restore.{RESET}")
        return

    print("\nChoose a hidden tool number to show again:")
    for index, tool_id in enumerate(hidden, 1):
        print(f"{CYAN}{index}.{RESET} {labels[tool_id]}")
    print(f"Type {YELLOW}'quit (q)'{RESET} to cancel.")
    raw = input("\n> ").strip().lower()

    if raw in ("", "quit", "q", "stop", "s"):
        print(f"{YELLOW}No changes made.{RESET}")
        return

    try:
        index = int(raw)
    except ValueError:
        print(f"{RED}Invalid entry.{RESET}")
        return

    if not 1 <= index <= len(hidden):
        print(f"{RED}Invalid entry.{RESET}")
        return

    tool_id = hidden[index - 1]
    new_hidden = [item for item in prefs["hidden"] if item != tool_id]
    save_directory_preferences(prefs["order"], new_hidden)
    print(f"{GREEN}{labels[tool_id]} restored to the directory.{RESET}")


def _view_saved_config():
    data = load_config()
    if not data:
        print(f"\n{YELLOW}No saved config values yet. Defaults are currently in use.{RESET}")
        return

    print(f"\n{YELLOW}Saved Config:{RESET}")
    print(json.dumps(data, indent=4))


def _reset_config():
    config_path = get_config_path()
    print(f"\n{YELLOW}Reset Config:{RESET}")
    print("This will wipe your saved settings and restore Termyx defaults.")
    print(f"Type {RED}reset{RESET} to confirm, or {YELLOW}'quit (q)'{RESET} to cancel.")
    choice = input("\n> ").strip().lower()

    if choice in ("", "quit", "q", "stop", "s"):
        print(f"{YELLOW}No changes made.{RESET}")
        return
    if choice != "reset":
        print(f"{RED}Invalid entry.{RESET}")
        return

    try:
        if os.path.exists(config_path):
            os.remove(config_path)
        print(f"{GREEN}Config reset to defaults.{RESET}")
    except OSError:
        print(f"{RED}Could not reset config.{RESET}")


def _export_config():
    data = load_config()
    if not data:
        print(f"{YELLOW}There are no saved config values to export yet.{RESET}")
        return

    print(f"\n{YELLOW}Export Config Preset:{RESET}")
    print("Enter a full file path ending in .json for the preset export.")
    print(f"Type {YELLOW}'quit (q)'{RESET} to cancel.")
    path = input("\n> ").strip().strip('"')

    if path.lower() in ("", "quit", "q", "stop", "s"):
        print(f"{YELLOW}No changes made.{RESET}")
        return
    if not path.lower().endswith(".json"):
        print(f"{RED}Preset exports must use a .json filename.{RESET}")
        return

    try:
        parent = os.path.dirname(path)
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"{GREEN}Config preset exported to {path}.{RESET}")
    except OSError:
        print(f"{RED}Could not export config preset.{RESET}")


def _import_config():
    print(f"\n{YELLOW}Import Config Preset:{RESET}")
    print("Enter the full path to a .json preset file to import.")
    print(f"Type {YELLOW}'quit (q)'{RESET} to cancel.")
    path = input("\n> ").strip().strip('"')

    if path.lower() in ("", "quit", "q", "stop", "s"):
        print(f"{YELLOW}No changes made.{RESET}")
        return

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            print(f"{RED}Preset file must contain a JSON object.{RESET}")
            return
        save_config(data)
        print(f"{GREEN}Config preset imported successfully.{RESET}")
    except FileNotFoundError:
        print(f"{RED}Preset file not found.{RESET}")
    except json.JSONDecodeError:
        print(f"{RED}Preset file is not valid JSON.{RESET}")
    except OSError:
        print(f"{RED}Could not import config preset.{RESET}")
