import ast
import math
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET

ALLOWED_FUNCTIONS = {
    "abs": abs,
    "round": round,
    "sqrt": math.sqrt,
    "log": math.log10,
    "ln": math.log,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
}

ALLOWED_CONSTANTS = {
    "pi": math.pi,
    "e": math.e,
}


def _evaluate(node):
    if isinstance(node, ast.Expression):
        return _evaluate(node.body)

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Unsupported constant")

    if isinstance(node, ast.BinOp):
        left = _evaluate(node.left)
        right = _evaluate(node.right)
        operators = {
            ast.Add: lambda a, b: a + b,
            ast.Sub: lambda a, b: a - b,
            ast.Mult: lambda a, b: a * b,
            ast.Div: lambda a, b: a / b,
            ast.FloorDiv: lambda a, b: a // b,
            ast.Mod: lambda a, b: a % b,
            ast.Pow: lambda a, b: a ** b,
        }
        handler = operators.get(type(node.op))
        if handler is None:
            raise ValueError("Unsupported operation")
        return handler(left, right)

    if isinstance(node, ast.UnaryOp):
        operand = _evaluate(node.operand)
        operators = {
            ast.UAdd: lambda value: +value,
            ast.USub: lambda value: -value,
        }
        handler = operators.get(type(node.op))
        if handler is None:
            raise ValueError("Unsupported unary operation")
        return handler(operand)

    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise ValueError("Unsupported function call")
        func = ALLOWED_FUNCTIONS.get(node.func.id)
        if func is None:
            raise ValueError("Unsupported function")
        if any(keyword.arg is None for keyword in node.keywords):
            raise ValueError("Unsupported function arguments")
        args = [_evaluate(arg) for arg in node.args]
        kwargs = {keyword.arg: _evaluate(keyword.value) for keyword in node.keywords}
        return func(*args, **kwargs)

    if isinstance(node, ast.Name):
        if node.id in ALLOWED_CONSTANTS:
            return ALLOWED_CONSTANTS[node.id]
        raise ValueError("Unknown value")

    raise ValueError("Unsupported expression")


def safe_eval(expression):
    tree = ast.parse(expression, mode="eval")
    return _evaluate(tree)


def run():
    try:
        print("\033]0;Termyx - Calculator\007", end="", flush=True)
        while True:
            print(f"{YELLOW}Let's crunch some numbers.{RESET}")
            print(f"\n{YELLOW}Supported operations:{RESET} + - * / ** // % abs() round(x, decimals) sqrt() log() ln()")
            print(f"{YELLOW}Trigonometric functions:{RESET} sin() cos() tan()")
            print(f"{YELLOW}Constants:{RESET} pi e")
            print("Enter your expression below (e.g. 2 * pi, sqrt(16), log(100), sin(pi/2)).")
            print("The calculator respects the order of operations and supports brackets.")
            try:
                expression = input(f"\n> ").strip()

                if not expression:
                    print(f"{RED}Please enter an expression.{RESET}")
                    continue

                result = safe_eval(expression)

                if isinstance(result, float):
                    result = round(result, 10)

                print(f"{GREEN}Your answer is {result}.{RESET}")

            except ZeroDivisionError:
                print(f"{RED}You can't divide by zero.{RESET}")
            except Exception:
                print(f"{RED}Invalid expression. Try again.{RESET}")

            again = input("\nAnother calculation? (Y/n):\n> ").strip().lower()
            if again not in ("y", "yes"):
                break
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Calculator interrupted.{RESET}")
