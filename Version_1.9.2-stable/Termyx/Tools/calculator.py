from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET


def run():
    try:
        while True:
            print(f"{YELLOW}Let's crunch some numbers.{RESET}")
            try:
                num1 = float(input("Please enter your first number:\n> "))
                print(f"""
{YELLOW}Available operations:{RESET}

+    - addition
-    - subtraction
*    - multiplication
/    - division
**   - exponentiation
sqrt - square root
%    - percentage (num2% of num1)
//   - floor division (integer division)""")
                operation = input("\nPlease enter the operation you would like to perform:\n> ").strip()

                if operation in ("sqrt", "%"):
                    num2 = None
                else:
                    num2 = float(input("Please enter your second number:\n> "))
            except ValueError:
                print(f"{RED}Numbers only. Try again.{RESET}")
                continue

            if operation == "+":
                print(f"{GREEN}Your answer is {num1 + num2}.{RESET}")
            elif operation == "-":
                print(f"{GREEN}Your answer is {num1 - num2}.{RESET}")
            elif operation == "*":
                print(f"{GREEN}Your answer is {num1 * num2}.{RESET}")
            elif operation == "/":
                if num2 == 0:
                    print(f"{RED}You can't divide by zero.{RESET}")
                else:
                    print(f"{GREEN}Your answer is {num1 / num2}.{RESET}")
            elif operation == "**":
                if num1 == 0 and num2 <= 0:
                    print(f"{RED}0 cannot be raised to zero or a negative power.{RESET}")
                elif num1 < 0 and not num2.is_integer():
                    print(f"{RED}Negative numbers cannot be raised to fractional powers.{RESET}")
                else:
                    print(f"{GREEN}Your answer is {num1 ** num2}.{RESET}")
            elif operation == "sqrt":
                if num1 < 0:
                    print(f"{RED}Square root of a negative number is not supported.{RESET}")
                else:
                    print(f"{GREEN}Your answer is {num1 ** 0.5}.{RESET}")
            elif operation == "%":
                try:
                    num2 = float(input("Please enter the percentage you would like to calculate. e.g., 50 for 50%:\n> "))
                except ValueError:
                    print(f"{RED}Numbers only. Try again.{RESET}")
                    continue
                print(f"{GREEN}Your answer is {num1 * (num2 / 100)}.{RESET}")
            elif operation == "//":
                if num2 == 0:
                    print(f"{RED}You can't divide by zero.{RESET}")
                else:
                    print(f"{GREEN}Your answer is {int(num1 // num2)}.{RESET}")
            else:
                print(f"{RED}Invalid operation.{RESET}")
                continue

            again = input("\nAnother calculation? (y/n):\n> ").strip().lower()
            if again not in ("y", "yes"):
                break
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Calculator interrupted.{RESET}")