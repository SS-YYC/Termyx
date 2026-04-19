import random
import time
import sys
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET

VALID_DICE = (4, 6, 8, 10, 12, 20, 100)

DICE_FACES = {
    1: [
        "+---------+",
        "|         |",
        "|    o    |",
        "|         |",
        "+---------+"
    ],
    2: [
        "+---------+",
        "|  o      |",
        "|         |",
        "|      o  |",
        "+---------+"
    ],
    3: [
        "+---------+",
        "|  o      |",
        "|    o    |",
        "|      o  |",
        "+---------+"
    ],
    4: [
        "+---------+",
        "|  o   o  |",
        "|         |",
        "|  o   o  |",
        "+---------+"
    ],
    5: [
        "+---------+",
        "|  o   o  |",
        "|    o    |",
        "|  o   o  |",
        "+---------+"
    ],
    6: [
        "+---------+",
        "|  o   o  |",
        "|  o   o  |",
        "|  o   o  |",
        "+---------+"
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
            print(f"{CYAN}{line}{RESET}")
        time.sleep(delay)

    sys.stdout.write("\033[5A")
    for line in DICE_FACES[result]:
        print(f"{GREEN}{line}{RESET}")


def animate_spinner(sides):
    delays = [0.05, 0.05, 0.07, 0.07, 0.10, 0.13, 0.17, 0.22, 0.28, 0.35]
    for i, delay in enumerate(delays):
        spin = SPINNER[i % len(SPINNER)]
        print(f"\r{CYAN}  Rolling d{sides}... {spin}  {RESET}", end="", flush=True)
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
                print("\033]0;Termyx - Dice Roller\007", end="", flush=True)
                print(f"{YELLOW}Let's roll.{RESET}")
                print(f"Enter {YELLOW}'quit (q)'{RESET} to quit.")
                raw_num_dice = input(f"{YELLOW}How many dice would you like to roll?{RESET}\n\n> ").strip().lower()
                if raw_num_dice in ("quit", "q", "stop", "s"):
                    break
                num_dice = int(raw_num_dice)
                if num_dice <= 0:
                    print(f"{RED}Please enter a number greater than 0.{RESET}")
                    continue
            except ValueError:
                print(f"{RED}Whole numbers only. Try again.{RESET}")
                continue

            print(f"\n{YELLOW}What type of die? ({', '.join(str(d) for d in VALID_DICE)}){RESET}")
            raw = input("\n> ").strip().lower().replace("d", "")
            if raw in ("quit", "q", "stop", "s"):
                break
            try:
                sides = int(raw)
            except ValueError:
                print(f"{RED}Please enter a valid die type.{RESET}")
                continue

            if sides not in VALID_DICE:
                print(f"{RED}Invalid die. Please choose from: {', '.join(str(d) for d in VALID_DICE)}{RESET}")
                continue

            print(f"\n{CYAN}Rolling {num_dice}d{sides}...{RESET}\n")
            time.sleep(0.3)

            results = []
            for i in range(num_dice):
                if num_dice > 1:
                    print(f"{YELLOW}Die {i + 1}:{RESET}")
                result = roll_single(sides)
                results.append(result)
                print(f"\n{GREEN}  Rolled: {result}{RESET}\n")
                if i < num_dice - 1:
                    time.sleep(0.3)

            if num_dice > 1:
                print(f"{CYAN}Individual rolls: {results}{RESET}")
                print(f"{GREEN}\n  Total: {sum(results)}{RESET}\n")
    except (KeyboardInterrupt, EOFError):
        print(f"\n{YELLOW}Dice Roller interrupted.{RESET}")
