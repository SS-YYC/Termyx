import urllib.request
import json
import re


def _parse_version_tag(tag):
    match = re.search(r"(\d+)\.(\d+)\.(\d+)", tag)
    if not match:
        return None
    return tuple(int(part) for part in match.groups())

def check_for_updates(current_version):
    try:
        url = "https://api.github.com/repos/SS-YYC/Termyx/releases/latest"
        req = urllib.request.Request(url, headers={"User-Agent": "Termyx"})
        with urllib.request.urlopen(req, timeout=3) as response:
            data = json.loads(response.read())
            latest = data["tag_name"]
            latest_version = _parse_version_tag(latest)
            current_parsed = _parse_version_tag(current_version)
            if latest_version is None:
                return None
            if current_parsed is None or latest_version > current_parsed:
                return latest
    except Exception:
        pass
    return None
