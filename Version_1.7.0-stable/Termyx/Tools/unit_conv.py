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
    while True:
        print("Welcome to the Unit Converter!")
        print("\nCategories: length (len) | mass (ms) | temperature (temp)")
        category = input("> ").strip().lower()

        if category not in ("length", "len", "mass", "temperature", "temp"):
            print("Invalid category.")
            continue

        if category in ("length", "len"):
            print(f"\nUnits: {', '.join(TO_METRES.keys())}")

            from_unit = input("From:\n> ").strip().lower()
            if from_unit not in TO_METRES:
                print("Invalid unit.")
                continue

            to_unit = input("To:\n> ").strip().lower()
            if to_unit not in TO_METRES:
                print("Invalid unit.")
                continue

            if from_unit == to_unit:
                print("Units are the same — no conversion needed.")
                continue

            try:
                value = float(input("Enter value:\n> "))
            except ValueError:
                print("Numbers only. Try again.")
                continue

            if value < 0:
                print("Length cannot be negative.")
                continue

            result = value * TO_METRES[from_unit] / TO_METRES[to_unit]
            print(f"\n{value} {from_unit} = {round(result, 6)} {to_unit}")

        elif category in ("mass", "ms"):
            print(f"\nUnits: {', '.join(TO_GRAMS.keys())}")

            from_unit = input("From:\n> ").strip().lower()
            if from_unit not in TO_GRAMS:
                print("Invalid unit.")
                continue

            to_unit = input("To:\n> ").strip().lower()
            if to_unit not in TO_GRAMS:
                print("Invalid unit.")
                continue

            if from_unit == to_unit:
                print("Units are the same — no conversion needed.")
                continue

            try:
                value = float(input("Enter value:\n> "))
            except ValueError:
                print("Numbers only. Try again.")
                continue

            if value < 0:
                print("Mass cannot be negative.")
                continue

            result = value * TO_GRAMS[from_unit] / TO_GRAMS[to_unit]
            print(f"\n{value} {from_unit} = {round(result, 6)} {to_unit}")

        elif category in ("temperature", "temp"):
            print("\nUnits: c, f")

            from_unit = input("From:\n> ").strip().lower()
            if from_unit not in ("c", "f"):
                print("Invalid unit. Please enter 'c' or 'f'.")
                continue

            to_unit = input("To:\n> ").strip().lower()
            if to_unit not in ("c", "f"):
                print("Invalid unit. Please enter 'c' or 'f'.")
                continue

            try:
                value = float(input("Enter value:\n> "))
            except ValueError:
                print("Numbers only. Try again.")
                continue

            result = convert_temperature(value, from_unit, to_unit)
            print(f"\n{value}°{from_unit.upper()} = {round(result, 6)}°{to_unit.upper()}")

        again = input("\nDo this again? (y/n):\n> ").strip().lower()
        if again not in ("y", "yes"):
            break