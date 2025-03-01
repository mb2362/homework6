"""
This module provides a command-line interface (CLI) for a simple calculator.

The calculator performs basic arithmetic operations: addition, subtraction, multiplication,
and division. It accepts user input via command-line arguments and includes exception 
handling for invalid inputs.

Usage:
    python main.py <num1> <num2> <operation>

Example:
    python main.py 5 3 add
    Output: "The result of 5 add 3 is equal to 8"

"""

import sys

def calculator(a, b, operation):
    """
    Perform basic arithmetic operations based on user input.

    Args:
        a (str): The first number as a string (will be converted to int).
        b (str): The second number as a string (will be converted to int).
        operation (str): The arithmetic operation ('add', 'subtract', 'multiply', 'divide').

    Returns:
        str: A formatted string representing the result or an error message.
    """
    try:
        a, b = int(a), int(b)
        result = None  # Store the result and return at the end

        if operation == 'add':
            result = f"The result of {a} add {b} is equal to {a + b}"
        if operation == 'subtract':
            result = f"The result of {a} subtract {b} is equal to {a - b}"
        if operation == 'multiply':
            result = f"The result of {a} multiply {b} is equal to {a * b}"
        if operation == 'divide':
            if b == 0:
                result = "An error occurred: Cannot divide by zero"
            else:
                result = f"The result of {a} divide {b} is equal to {a // b}"
        if result is None:
            result = f"Unknown operation: {operation}"
    except ValueError:
        result = f"Invalid number input: {a} or {b} is not a valid number."

    return result  # Return the result once

if __name__ == "__main__":
    # Entry point for the command-line calculator
    if len(sys.argv) != 4:
        print("Usage: python main.py <num1> <num2> <operation>")
    else:
        print(calculator(sys.argv[1], sys.argv[2], sys.argv[3]))
