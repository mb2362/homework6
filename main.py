# main.py
from app import App   
import sys
from calculator import Calculator
from calculator.calculation import Calculation

def parse_args(args):
    """
    Parses the command-line arguments.
    Expected arguments: a, b, operation
    Returns a tuple (a, b, operation) with a and b as floats if valid.
    """
    if len(args) != 3:
        raise ValueError("Please provide exactly three arguments: a, b, and operation.")

    a_str, b_str, operation = args

    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        raise ValueError(f"Invalid number input: {a_str} or {b_str} is not a valid number.")
    
    return a, b, operation

def perform_operation(a, b, operation):
    """
    Maps the operation string to the corresponding Calculator method.
    """
    if operation == 'add':
        return Calculator.add(a, b)
    elif operation == 'subtract':
        return Calculator.subtract(a, b)
    elif operation == 'multiply':
        return Calculator.multiply(a, b)
    elif operation == 'divide':
        try:
            return Calculator.divide(a, b)
        except ZeroDivisionError:
            raise ZeroDivisionError("Cannot divide by zero.")
    else:
        raise ValueError(f"Unknown operation: {operation}")

def main():
    try:
        # Exclude the script name and Parse arguments
        a, b, operation = parse_args(sys.argv[1:])
        result = perform_operation(a, b, operation)
        print(f"The result of {int(a)} {operation} {int(b)} is equal to {result}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":

    app = App()
    app.start()