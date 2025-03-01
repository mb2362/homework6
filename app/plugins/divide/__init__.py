# DIVISION
from app.commands import CLI
from calculator import Calculator

class divideCommand(CLI):
    def execute(self, args):
        if len(args) != 2:
            print("Usage: divide <a> <b>")
            return
        try:
            a, b = float(args[0]), float(args[1])
            if b == 0:
                print("An error occurred: Cannot divide by zero.")
                return
            result = Calculator.divide(a, b)
            print(f"The result of {int(a)} / {int(b)} is equal to {result}")
        except ValueError:
            print(f"Invalid number input: {args[0]} or {args[1]} is not a valid number.")
