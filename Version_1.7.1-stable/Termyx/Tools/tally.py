import sys

def run():
    try:
        while True:
            print("Welcome to the Tally Counter!")
            count = 0
            print("Hit enter to increase the count by 1. To end the counter, type 'stop' and hit enter.")
            while True:
                print(f"The count is currently at {count}.")
                tc_value = input("> ")
                if tc_value.strip().lower() == "stop":
                    print()
                    break
                count += 1
                sys.stdout.write("\033[2A")
                sys.stdout.flush()

            print(f"Final count: {count}")
            again = input("\nDo this again? (y/n):\n> ").strip().lower()
            if again not in ("y", "yes"):
                break
    except KeyboardInterrupt:
        print("\nTally Counter interrupted.")