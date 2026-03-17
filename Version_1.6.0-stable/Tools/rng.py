import random


def run():
    while True:
        try:
            print("Note: negative numbers are allowed - just make sure the upper limit is greater than the lower limit. Whole numbers only.")
            lower = int(input("Enter the lower limit number:\n> "))
            upper = int(input("Enter the upper limit number:\n> "))
        except ValueError:
            print("Whole numbers only. Try again.")
            continue

        if lower >= upper:
            print("The upper limit must be greater than the lower limit.")
            continue

        print(f"Your random number is: {random.randint(lower, upper)}")

        again = input("\nDo this again? (y/n):\n> ").strip().lower()
        if again not in ("y", "yes"):
            break