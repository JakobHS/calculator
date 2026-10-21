#Calculator entirely made by claude (just comparing claude to me ;(  )
 
import ast
import operator
import tkinter as tk

# Operators the calculator is allowed to evaluate (safer than plain eval)
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def safe_eval(expression):
    """Evaluate a basic math expression without running arbitrary code."""

    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
            return OPERATORS[type(node.op)](_eval(node.left), _eval(node.right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in OPERATORS:
            return OPERATORS[type(node.op)](_eval(node.operand))
        raise ValueError("Invalid expression")

    return _eval(ast.parse(expression, mode="eval"))


class Calculator:
    BG = "#1e1e1e"
    DISPLAY_BG = "#2d2d2d"
    NUM_BG = "#3c3c3c"
    OP_BG = "#ff9500"
    FUNC_BG = "#a5a5a5"
    FG = "#ffffff"

    # (label, row, column, columnspan)
    BUTTONS = [
        ("C", 1, 0, 1), ("⌫", 1, 1, 1), ("%", 1, 2, 1), ("÷", 1, 3, 1),
        ("7", 2, 0, 1), ("8", 2, 1, 1), ("9", 2, 2, 1), ("×", 2, 3, 1),
        ("4", 3, 0, 1), ("5", 3, 1, 1), ("6", 3, 2, 1), ("−", 3, 3, 1),
        ("1", 4, 0, 1), ("2", 4, 1, 1), ("3", 4, 2, 1), ("+", 4, 3, 1),
        ("±", 5, 0, 1), ("0", 5, 1, 1), (".", 5, 2, 1), ("=", 5, 3, 1),
    ]

    # Map display symbols to the Python operators used for evaluation
    SYMBOLS = {"÷": "/", "×": "*", "−": "-"}

    def __init__(self, root):
        self.root = root
        self.root.title("Claude Calculator")
        self.root.configure(bg=self.BG)
        self.root.resizable(False, False)

        self.expression = ""
        self.just_evaluated = False

        self.history_var = tk.StringVar(value="")
        self.display_var = tk.StringVar(value="0")

        self._build_display()
        self._build_buttons()
        self._bind_keys()

    def _build_display(self):
        tk.Label(
            self.root, textvariable=self.history_var, anchor="e",
            bg=self.DISPLAY_BG, fg="#9a9a9a", font=("Segoe UI", 12), padx=12,
        ).grid(row=0, column=0, columnspan=4, sticky="nsew", pady=(10, 0), padx=10)

        tk.Label(
            self.root, textvariable=self.display_var, anchor="e",
            bg=self.DISPLAY_BG, fg=self.FG, font=("Segoe UI", 32, "bold"),
            padx=12, pady=10, width=12,
        ).grid(row=0, column=0, columnspan=4, sticky="sew", pady=(35, 10), padx=10)

    def _build_buttons(self):
        for label, row, col, span in self.BUTTONS:
            if label in ("÷", "×", "−", "+", "="):
                bg = self.OP_BG
            elif label in ("C", "⌫", "%"):
                bg = self.FUNC_BG
            else:
                bg = self.NUM_BG

            tk.Button(
                self.root, text=label, command=lambda l=label: self.on_press(l),
                bg=bg, fg=self.FG, activebackground="#555555", activeforeground=self.FG,
                font=("Segoe UI", 18), relief="flat", bd=0, width=4, height=2,
            ).grid(row=row, column=col, columnspan=span, sticky="nsew", padx=4, pady=4)

        self.root.grid_rowconfigure(6, minsize=6)

    def _bind_keys(self):
        for key in "0123456789.+-*/%":
            self.root.bind(key, lambda e, k=key: self.on_press(k))
        self.root.bind("<Return>", lambda e: self.on_press("="))
        self.root.bind("<KP_Enter>", lambda e: self.on_press("="))
        self.root.bind("=", lambda e: self.on_press("="))
        self.root.bind("<BackSpace>", lambda e: self.on_press("⌫"))
        self.root.bind("<Escape>", lambda e: self.on_press("C"))

    def on_press(self, key):
        key = self.SYMBOLS.get(key, key)

        if key == "C":
            self.expression = ""
            self.history_var.set("")
        elif key == "⌫":
            self.expression = self.expression[:-1]
        elif key == "=":
            self.evaluate()
            return
        elif key == "±":
            self.toggle_sign()
        else:
            # Start fresh if typing a number right after a result
            if self.just_evaluated and key not in "+-*/%":
                self.expression = ""
            # Don't allow two operators in a row; replace the previous one
            if key in "+*/%" and self.expression[-1:] in "+-*/%":
                self.expression = self.expression[:-1]
            self.expression += key

        self.just_evaluated = False
        self.display_var.set(self.pretty(self.expression) or "0")

    def toggle_sign(self):
        if not self.expression:
            return
        if self.expression.startswith("-(") and self.expression.endswith(")"):
            self.expression = self.expression[2:-1]
        else:
            self.expression = f"-({self.expression})"

    def evaluate(self):
        if not self.expression:
            return
        try:
            result = safe_eval(self.expression)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            elif isinstance(result, float):
                result = round(result, 10)
            self.history_var.set(self.pretty(self.expression) + " =")
            self.expression = str(result)
            self.display_var.set(self.expression)
        except ZeroDivisionError:
            self.display_var.set("Can't ÷ by 0")
            self.expression = ""
        except (ValueError, SyntaxError, OverflowError):
            self.display_var.set("Error")
            self.expression = ""
        self.just_evaluated = True

    def pretty(self, expr):
        return expr.replace("/", "÷").replace("*", "×").replace("-", "−")


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
