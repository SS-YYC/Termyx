import random
import time
import sys

VALID_DICE = (4, 6, 8, 10, 12, 20, 100)

DICE_FACES = {
    1: [
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ],
    2: [
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ],
    3: [
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ],
    4: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ],
    5: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ],
    6: [
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    ]
}

SPINNER = ["|", "/", "-", "\\"]


def animate_d6(result):
    delays = [0.05, 0.05, 0.07, 0.07, 0.10, 0.13, 0.17, 0.22, 0.28, 0.35]
    for i, delay in enumerate(delays):
        face = DICE_FACES[random.randint(1, 6)]
        if i > 0:
            sys.stdout.write("\033[5A")
        for line in face:
            print(line)
        time.sleep(delay)

    sys.stdout.write("\033[5A")
    for line in DICE_FACES[result]:
        print(line)


def animate_spinner(sides):
    delays = [0.05, 0.05, 0.07, 0.07, 0.10, 0.13, 0.17, 0.22, 0.28, 0.35]
    for i, delay in enumerate(delays):
        spin = SPINNER[i % len(SPINNER)]
        print(f"\r  Rolling d{sides}... {spin}  ", end="", flush=True)
        time.sleep(delay)
    print(f"\r                          ", end="", flush=True)


def roll_single(sides):
    result = random.randint(1, sides)
    print()
    if sides == 6:
        animate_d6(result)
    else:
        animate_spinner(sides)
    return result


def run():
    try:
        while True:
            try:
                print("Welcome to the Dice Roller!")
                num_dice = int(input("\nHow many dice would you like to roll?\n> "))
                if num_dice <= 0:
                    print("Please enter a number greater than 0.")
                    continue
            except ValueError:
                print("Whole numbers only. Try again.")
                continue

            print(f"\nWhat type of die? ({', '.join(str(d) for d in VALID_DICE)})")
            raw = input("> ").strip().lower().replace("d", "")
            try:
                sides = int(raw)
            except ValueError:
                print("Please enter a valid die type.")
                continue

            if sides not in VALID_DICE:
                print(f"Invalid die. Please choose from: {', '.join(str(d) for d in VALID_DICE)}")
                continue

            print(f"\nRolling {num_dice}d{sides}...\n")
            time.sleep(0.3)

            results = []
            for i in range(num_dice):
                if num_dice > 1:
                    print(f"Die {i + 1}:")
                result = roll_single(sides)
                results.append(result)
                print(f"\n  Rolled: {result}\n")
                if i < num_dice - 1:
                    time.sleep(0.3)

            if num_dice > 1:
                print(f"  Individual rolls: {results}")
                print(f"  Total: {sum(results)}\n")

            again = input("\nDo this again? (y/n):\n> ").strip().lower()
            if again not in ("y", "yes"):
                break
    except KeyboardInterrupt:
        print("\nDice Roller interrupted.")