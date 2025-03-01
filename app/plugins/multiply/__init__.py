# MULTIPLICATION
from app.commands import CLI
from calculator import Calculator

class multiplyCommand(CLI):
    def execute(self, args):
        if len(args) != 2:
            print("Usage: multiply <a> <b>")
            return
        try:
            a = float(args[0])
            b = float(args[1])
            result = Calculator.multiply(a, b)
            print(f"The result of {int(a)} x {int(b)} is equal to {result}")
        except ValueError:
            print(f"Invalid number input: {args[0]} or {args[1]} is not a valid number.")
        except ZeroDivisionError:
            print("An error occurred: Cannot divide by zero.")