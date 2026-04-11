from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET

TO_METRES = {
    "mm": 0.001,
    "cm": 0.01,
    "m":  1,
    "km": 1000,
}

TO_GRAMS = {
    "mg": 0.001,
    "g":  1,
    "kg": 1000,
}


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "c":
        return (value * 9/5) + 32
    else:
        return (value - 32) * 5/9


def run():
    try:
        print("\033]0;Termyx - Unit Converter\007", end="", flush=True)
        while True:
            print(f"{YELLOW}Lost in units?{RESET}")
            print(f"\n{YELLOW}Categories: length (len/l) | mass (ms/m) | temperature (temp/t){RESET}")
            print(f"Enter {YELLOW}'quit (q)'{RESET} to quit.")
            category = input("\n> ").strip().lower()

            if category in ("quit", "q", "stop", "s"):
                break

            if category not in ("length", "len", "l", "mass", "ms", "m", "temperature", "temp", "t"):
                print(f"{RED}Invalid category.{RESET}")
                continue

            if category in ("length", "len", "l"):
                print(f"\n{YELLOW}Units: {', '.join(TO_METRES.keys())}{RESET}")

                from_unit = input("From:\n\n> ").strip().lower()
                if from_unit in ("quit", "q", "stop", "s"):
                    break
                if from_unit not in TO_METRES:
                    print(f"{RED}Invalid unit.{RESET}")
                    continue

                to_unit = input("To:\n\n> ").strip().lower()
                if to_unit in ("quit", "q", "stop", "s"):
                    break
                if to_unit not in TO_METRES:
                    print(f"{RED}Invalid unit.{RESET}")
                    continue

                if from_unit == to_unit:
                    print(f"{YELLOW}The units are the same, so no conversion is needed.{RESET}")
                    continue

                try:
                    value_raw = input("Enter value:\n\n> ").strip()
                    if value_raw.lower() in ("quit", "q", "stop", "s"):
                        break
                    value = float(value_raw)
                except ValueError:
                    print(f"{RED}Numbers only. Try again.{RESET}")
                    continue

                if value < 0:
                    print(f"{RED}Length cannot be negative.{RESET}")
                    continue

                result = value * TO_METRES[from_unit] / TO_METRES[to_unit]
                print(f"\n{GREEN}{value} {from_unit} = {round(result, 6)} {to_unit}{RESET}")

            elif category in ("mass", "ms", "m"):
                print(f"\n{YELLOW}Units: {', '.join(TO_GRAMS.keys())}{RESET}")

                from_unit = input("From:\n\n> ").strip().lower()
                if from_unit in ("quit", "q", "stop", "s"):
                    break
                if from_unit not in TO_GRAMS:
                    print(f"{RED}Invalid unit.{RESET}")
                    continue

                to_unit = input("To:\n\n> ").strip().lower()
                if to_unit in ("quit", "q", "stop", "s"):
                    break
                if to_unit not in TO_GRAMS:
                    print(f"{RED}Invalid unit.{RESET}")
                    continue

                if from_unit == to_unit:
                    print(f"{YELLOW}The units are the same, so no conversion is needed.{RESET}")
                    continue

                try:
                    value_raw = input("Enter value:\n\n> ").strip()
                    if value_raw.lower() in ("quit", "q", "stop", "s"):
                        break
                    value = float(value_raw)
                except ValueError:
                    print(f"{RED}Numbers only. Try again.{RESET}")
                    continue

                if value < 0:
                    print(f"{RED}Mass cannot be negative.{RESET}")
                    continue

                result = value * TO_GRAMS[from_unit] / TO_GRAMS[to_unit]
                print(f"\n{GREEN}{value} {from_unit} = {round(result, 6)} {to_unit}{RESET}")

            elif category in ("temperature", "temp", "t"):
                print(f"\n{YELLOW}Units: c, f{RESET}")

                from_unit = input("From:\n\n> ").strip().lower()
                if from_unit in ("quit", "q", "stop", "s"):
                    break
                if from_unit not in ("c", "f"):
                    print(f"{RED}Invalid unit. Please enter 'c' or 'f'.{RESET}")
                    continue

                to_unit = input("To:\n\n> ").strip().lower()
                if to_unit in ("quit", "q", "stop", "s"):
                    break
                if to_unit not in ("c", "f"):
                    print(f"{RED}Invalid unit. Please enter 'c' or 'f'.{RESET}")
                    continue

                try:
                    value_raw = input("Enter value:\n\n> ").strip()
                    if value_raw.lower() in ("quit", "q", "stop", "s"):
                        break
                    value = float(value_raw)
                except ValueError:
                    print(f"{RED}Numbers only. Try again.{RESET}")
                    continue

                result = convert_temperature(value, from_unit, to_unit)
                print(f"\n{GREEN}{value} deg {from_unit.upper()} = {round(result, 6)} deg {to_unit.upper()}{RESET}")
    except (KeyboardInterrupt, EOFError):
        print(f"\n{YELLOW}Unit Converter interrupted.{RESET}")
