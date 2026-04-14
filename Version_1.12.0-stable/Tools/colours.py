from Tools.config_store import load_config, save_config


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
    },
    "forest": {
        "primary": "\033[32m",   # dark green
        "success": "\033[92m",   # bright green
        "error":   "\033[91m",   # red
        "accent":  "\033[33m",   # dark yellow/brown
        "reset":   "\033[0m"
    },
    "amber": {
        "primary": "\033[93m",   # bright amber/yellow
        "success": "\033[33m",   # dark amber
        "error":   "\033[91m",   # red
        "accent":  "\033[97m",   # white
        "reset":   "\033[0m"
    },
    "dracula": {
        "primary": "\033[95m",   # magenta/purple
        "success": "\033[92m",   # green
        "error":   "\033[93m",   # yellow
        "accent":  "\033[94m",   # blue
        "reset":   "\033[0m"
    }
}

THEME_DESCRIPTIONS = {
    "default":     "The classic Termyx experience. Warm and familiar.",
    "ocean":       "Cool blues and greens. Easy on the eyes.",
    "ember":       "Reds and warm tones. Bold and intense.",
    "neon":        "Bright magentas and cyans. High contrast and vibrant.",
    "monochrome":  "No colour distractions. Clean and minimal.",
    "forest":      "Deep greens and earthy tones. Calm and grounded.",
    "amber":       "Warm ambers and whites. Retro and nostalgic.",
    "dracula":     "Purples and greens. Dark and mysterious."
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
    return load_config().get("theme", "default")


def save_theme(name):
    data = load_config()
    data["theme"] = name
    save_config(data)


set_theme(load_theme())
