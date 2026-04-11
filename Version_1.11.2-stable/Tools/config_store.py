import json
import os


APP_NAME = "Termyx"
LEGACY_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config.json")


def get_config_dir():
    if os.name == "nt":
        base = os.getenv("APPDATA") or os.path.join(os.path.expanduser("~"), "AppData", "Roaming")
    else:
        base = os.getenv("XDG_CONFIG_HOME") or os.path.join(os.path.expanduser("~"), ".config")
    return os.path.join(base, APP_NAME)


def get_config_path():
    return os.path.join(get_config_dir(), "config.json")


def _read_json(path):
    try:
        with open(path, "r") as f:
            data = json.load(f)
        if isinstance(data, dict):
            return data
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        pass
    return {}


def load_config():
    config_path = get_config_path()
    data = _read_json(config_path)
    if data:
        return data

    legacy_data = _read_json(LEGACY_CONFIG_PATH)
    if legacy_data:
        try:
            save_config(legacy_data)
        except OSError:
            pass
        return legacy_data

    return {}


def save_config(data):
    config_dir = get_config_dir()
    os.makedirs(config_dir, exist_ok=True)
    with open(get_config_path(), "w") as f:
        json.dump(data, f, indent=4)
