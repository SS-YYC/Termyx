# Developer Guide

This page is for developers who want to contribute to or modify Termyx. It covers the project structure, conventions, and things to keep in mind when adding or changing code.

---

## Project Structure

```
Version_x.x.x-stable/
├── termyx.bat
├── termyx.sh
└── Termyx/
    ├── main.py
    ├── changelog.md
    └── Tools/
        ├── __init__.py
        ├── colours.py
        ├── timer.py
        ├── stopwatch.py
        ├── calculator.py
        ├── tally.py
        ├── system_stats.py
        ├── rng.py
        ├── dice.py
        ├── unit_conv.py
        ├── pom_tmr.py
        └── coin_flip.py
```

`main.py` is the entry point. Each tool lives in its own file inside `Tools/`. `colours.py` defines the ANSI colour variables used across all tools.

---

## Adding a New Tool

Every new tool follows the same pattern:

**1. Create a new file** in `Tools/` — e.g. `Tools/my_tool.py`

**2. Wrap all logic in a `run()` function.** The function must be named `run()` — this is what `main.py` calls.

**3. Import colours** at the top of the file:
```python
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET
```

**4. Follow the standard structure:**
```python
def run():
    try:
        while True:
            print(f"{YELLOW}Welcome to the [Tool Name]!{RESET}")
            # tool logic here
            again = input("\nDo this again? (y/n):\n> ").strip().lower()
            if again not in ("y", "yes"):
                break
    except KeyboardInterrupt:
        print(f"\n{YELLOW}[Tool Name] interrupted.{RESET}")
```

**5. Register the tool in `main.py`:**
- Add the import: `from Tools import ..., my_tool`
- Add to `valid_commands`: `"my tool", "mt"`
- Add to the directory print block: `{CYAN}- My Tool (mt){RESET}`
- Add to the helplinks string: `- My Tool (mt) - Description here.`
- Add to the routing block: `elif choice in ("my tool", "mt"): my_tool.run()`

---

## Colour Conventions

All tools must use the colour system from `Tools/colours.py`. Follow these rules consistently:

| Colour | Use for |
|--------|---------|
| `YELLOW` | Welcome messages, headers, mode/category prompts, interruption messages |
| `RED` | Errors and invalid input |
| `GREEN` | Successful results and positive outcomes |
| `CYAN` | Live values, active displays, tool names in directory |
| `RESET` | Always append after every coloured string |

Never hardcode ANSI codes directly — always import from `colours.py`.

---

## Keyboard Interrupt Handling

Every tool must handle `KeyboardInterrupt` gracefully. Wrap the main `while True` loop in a `try/except`:

```python
try:
    while True:
        # tool logic
except KeyboardInterrupt:
    print(f"\n{YELLOW}[Tool Name] interrupted.{RESET}")
```

This allows CTRL+C to exit the tool cleanly and return to the directory rather than crashing the app.

---

## "Do this again?" Logic

Every tool must end with the standard again prompt:

```python
again = input("\nDo this again? (y/n):\n> ").strip().lower()
if again not in ("y", "yes"):
    break
```

Accept both `y` and `yes`. The `break` exits the `while True` loop and returns control to `main.py`, which automatically redisplays the directory.

---

## Threading

Tools that run background processes (stopwatch, system stats) use Python's `threading` module. Key things to keep in mind:

- Always use `daemon=True` when creating threads so they don't block the app from exiting
- Use a global `running` or `monitor_running` flag to control the thread loop
- Always call `thread.join()` before breaking out of the command loop to ensure the thread stops cleanly

---

## Platform Considerations

Termyx targets **Windows 10+** primarily but should work on macOS and Linux. Keep these in mind:

- ANSI colour codes are enabled on Windows via `os.system("")` in `main.py` — do not remove this
- Avoid hardcoding Windows-specific paths. Use `os.name != 'nt'` checks where needed (see `system_stats.py` for an example)
- The `\a` beep character may be silent on some macOS/Linux terminals — this is expected behaviour

---

## Versioning

Termyx uses semantic versioning — `MAJOR.MINOR.PATCH`:

- **MAJOR** — large new features or breaking changes
- **MINOR** — new tools or significant feature additions
- **PATCH** — bug fixes and minor improvements

Update the version number in the splash screen in `main.py` with every release.

---

## Questions or Contributions

- 💬 [Join the Discord Server](https://discord.gg/GxPxfjGAef)
- 🐛 [Open an Issue on GitHub](https://github.com/SS-YYC/Termyx)
