THEMES = {
    "default": {
        "primary": "\033[93m",   # yellow
        "success": "\033[92m",   # green
        "error":   "\033[91m",   # red
        "accent":  "\033[96m",   # cyan
        "reset":   "\033[0m"
    },
    "ocean": {
        "primary": "\033[96m",   # cyan
        "success": "\033[94m",   # blue
        "error":   "\033[91m",   # red
        "accent":  "\033[92m",   # green
        "reset":   "\033[0m"
    },
    "ember": {
        "primary": "\033[91m",   # bright red
        "success": "\033[93m",   # yellow
        "error":   "\033[95m",   # magenta
        "accent":  "\033[33m",   # orange
        "reset":   "\033[0m"
    },
    "neon": {
        "primary": "\033[95m",   # magenta
        "success": "\033[96m",   # cyan
        "error":   "\033[91m",   # red
        "accent":  "\033[92m",   # green
        "reset":   "\033[0m"
    },
    "monochrome": {
        "primary": "\033[97m",   # bright white
        "success": "\033[97m",   # bright white
        "error":   "\033[97m",   # bright white
        "accent":  "\033[97m",   # bright white
        "reset":   "\033[0m"
    }
}

THEME_DESCRIPTIONS = {
    "default":     "The classic Termyx experience. Warm and familiar.",
    "ocean":       "Cool blues and greens. Easy on the eyes.",
    "ember":       "Reds and warm tones. Bold and intense.",
    "neon":        "Bright magentas and cyans. High contrast and vibrant.",
    "monochrome":  "No colour distractions. Clean and minimal."
}

def set_theme(name):
    global YELLOW, GREEN, RED, CYAN, RESET
    t = THEMES.get(name, THEMES["default"])
    YELLOW = t["primary"]
    GREEN  = t["success"]
    RED    = t["error"]
    CYAN   = t["accent"]
    RESET  = t["reset"]


def load_theme():
    import json
    import os
    config = os.path.join(os.path.dirname(__file__), "..", "config.json")
    try:
        with open(config, "r") as f:
            return json.load(f).get("theme", "default")
    except FileNotFoundError:
        return "default"


def save_theme(name):
    import json
    import os
    config = os.path.join(os.path.dirname(__file__), "..", "config.json")
    with open(config, "w") as f:
        json.dump({"theme": name}, f)

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
    print(f"{GREEN}* = current theme{RESET}")
    t = input("\n> ").strip().lower()
    if t in THEMES:
        set_theme(t)
        save_theme(t)
        print(f"{GREEN}Theme set to {t}. Restart Termyx to apply.{RESET}")
    elif t == "":
        print(f"{YELLOW}No changes made.{RESET}")
    else:
        print(f"{RED}Invalid theme.{RESET}")


set_theme(load_theme())
