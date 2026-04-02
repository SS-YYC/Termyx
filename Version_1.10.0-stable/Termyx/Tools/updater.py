import urllib.request
import json

def check_for_updates(current_version):
    try:
        url = "https://api.github.com/repos/SS-YYC/Termyx/releases/latest"
        req = urllib.request.Request(url, headers={"User-Agent": "Termyx"})
        with urllib.request.urlopen(req, timeout=3) as response:
            data = json.loads(response.read())
            latest = data["tag_name"]
            if latest != current_version:
                return latest
    except Exception:
        pass
    return None