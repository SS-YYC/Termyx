import secrets
import string
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET

def generate_password(length, use_upper, use_digits, use_symbols):
    pool = string.ascii_lowercase
    if use_upper:
        pool += string.ascii_uppercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation
    return "".join(secrets.choice(pool) for _ in range(length))

def run():
    print("\033]0;Termyx - Password Generator\007", end="", flush=True)
    try:
        print(f"{YELLOW}A strong password, coming right up.{RESET}")
        print(f"Enter {YELLOW}'quit (q)'{RESET} to return.")
        while True:
            try:
                length_input = input("Enter desired password length (8-128):\n\n> ").strip()
                if length_input.lower() in ("quit", "q", "stop", "s"):
                    break
                length = int(length_input)
                if not 8 <= length <= 128:
                    print(f"{RED}Length must be between 8 and 128.{RESET}")
                    continue
            except ValueError:
                print(f"{RED}Please enter a valid number for the length.{RESET}")
                continue

            upper_raw = input("Include uppercase letters? (y/n):\n\n> ").strip().lower()
            if upper_raw in ("quit", "q", "stop", "s"):
                break
            use_upper = upper_raw == "y"

            digits_raw = input("Include digits? (y/n):\n\n> ").strip().lower()
            if digits_raw in ("quit", "q", "stop", "s"):
                break
            use_digits = digits_raw == "y"

            symbols_raw = input("Include symbols? (y/n):\n\n> ").strip().lower()
            if symbols_raw in ("quit", "q", "stop", "s"):
                break
            use_symbols = symbols_raw == "y"

            if not any([use_upper, use_digits, use_symbols]):
                print(f"{RED}At least one character type must be included.{RESET}")
                continue

            password = generate_password(length, use_upper, use_digits, use_symbols)
            print(f"\n{GREEN}Generated password: {password}{RESET}\n")
    except (KeyboardInterrupt, EOFError):
        print(f"\n{YELLOW}Password Generator interrupted.{RESET}")
