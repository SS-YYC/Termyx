def run():
    while True:
        try:
            num1 = float(input("Please enter your first number:\n> "))
            print("""
Available operations:

+    - addition
-    - subtraction
*    - multiplication
/    - division
**   - exponentiation
sqrt - square root
%    - percentage (num2% of num1)
//   - floor division (integer division)""")
            operation = input("\nPlease enter the operation you would like to perform:\n> ")

            if operation.strip() in ("sqrt", "%"):
                num2 = None
            else:
                num2 = float(input("Please enter your second number:\n> "))
        except ValueError:
            print("Numbers only. Try again.")
            continue

        if operation.strip() == "+":
            print(f"Your answer is {num1 + num2}.")
        elif operation.strip() == "-":
            print(f"Your answer is {num1 - num2}.")
        elif operation.strip() == "*":
            print(f"Your answer is {num1 * num2}.")
        elif operation.strip() == "/":
            if num2 == 0:
                print("You can't divide by zero.")
            else:
                print(f"Your answer is {num1 / num2}.")
        elif operation.strip() == "**":
            if num1 == 0 and num2 <= 0:
                print("0 cannot be raised to zero or a negative power.")
            elif num1 < 0 and not num2.is_integer():
                print("Negative numbers cannot be raised to fractional powers.")
            elif num1 == 0 and num2 > 0:
                print("Your answer is 0.")
            else:
                print(f"Your answer is {num1 ** num2}.")
        elif operation.strip() == "sqrt":
            if num1 < 0:
                print("Square root of a negative number is not supported.")
            else:
                print(f"Your answer is {num1 ** 0.5}.")
        elif operation.strip() == "%":
            try:
                num2 = float(input("Please enter the percentage you would like to calculate. e.g., 50 for 50%:\n> "))
            except ValueError:
                print("Numbers only. Try again.")
                continue
            print(f"Your answer is {num1 * (num2 / 100)}.")
        elif operation.strip() == "//":
            if num2 == 0:
                print("You can't divide by zero.")
            else:
                print(f"Your answer is {int(num1 // num2)}.")
        else:
            print("Invalid operation.")
            continue

        again = input("\nDo this again? (y/n):\n> ").strip().lower()
        if again not in ("y", "yes"):
            break