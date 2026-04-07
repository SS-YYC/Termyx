import ast
import math
from Tools.colours import RED, GREEN, YELLOW, CYAN, RESET
from Tools.config_store import load_config, save_config

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

HISTORY_LIMIT = 5
HISTORY_COMMANDS = {"history", "hist", "h"}


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


def _load_history():
    history = load_config().get("calculator_history", [])
    if isinstance(history, list):
        return [str(item) for item in history[-HISTORY_LIMIT:]]
    return []


def _save_result(result):
    data = load_config()
    history = data.get("calculator_history", [])
    if not isinstance(history, list):
        history = []
    history.append(str(result))
    data["calculator_history"] = history[-HISTORY_LIMIT:]
    try:
        save_config(data)
    except OSError:
        print(f"{RED}Could not save calculator history.{RESET}")


def run():
    try:
        print("\033]0;Termyx - Calculator\007", end="", flush=True)
        while True:
            print(f"{YELLOW}Let's crunch some numbers.{RESET}")
            print(f"\n{YELLOW}Supported operations:{RESET} + - * / ** // % abs() round(x, decimals) sqrt() log() ln()")
            print(f"{YELLOW}Trigonometric functions:{RESET} sin() cos() tan()")
            print(f"{YELLOW}Constants:{RESET} pi e")
            print("Enter an expression below (e.g. 2 * pi, sqrt(16), log(100), sin(pi/2)).")
            print("The calculator respects the order of operations and supports brackets.")
            print(f"Enter {YELLOW}'history (h)'{RESET} to view the last {HISTORY_LIMIT} answers.")
            print(f"Enter {YELLOW}'quit (q)'{RESET} to quit.")
            try:
                expression = input(f"\n> ").strip()

                if expression.lower() in ("quit", "q", "stop", "s"):
                    break
                if expression.lower() in HISTORY_COMMANDS:
                    history = _load_history()
                    if history:
                        print(f"{YELLOW}Recent answers:{RESET} {', '.join(history)}")
                    else:
                        print(f"{YELLOW}No calculator history yet.{RESET}")
                    continue

                if not expression:
                    print(f"{RED}Please enter an expression.{RESET}")
                    continue

                result = safe_eval(expression)

                if isinstance(result, float):
                    result = round(result, 10)

                print(f"{GREEN}Result: {result}{RESET}")
                _save_result(result)

            except ZeroDivisionError:
                print(f"{RED}You can't divide by zero.{RESET}")
            except Exception:
                print(f"{RED}Invalid expression. Try again.{RESET}")
    except (KeyboardInterrupt, EOFError):
        print(f"\n{YELLOW}Calculator interrupted.{RESET}")
