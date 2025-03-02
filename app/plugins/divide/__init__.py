# DIVISION
import logging
from app.commands import CLI
from calculator import Calculator

# Configure logger
logger = logging.getLogger(__name__)

class divideCommand(CLI):
    def execute(self, args):
        if len(args) != 2:
            logger.warning("Invalid arguments for divide command. Expected 2 arguments.")
            print("Usage: divide <a> <b>")
            return
        try:
            a, b = float(args[0]), float(args[1])
            if b == 0:
                logger.error("Division by zero attempted.")
                print("An error occurred: Cannot divide by zero.")
                return
            result = Calculator.divide(a, b)
            logger.info(f"Division executed: {a} / {b} = {result}")
            print(f"The result of {int(a)} / {int(b)} is equal to {result}")
        except ValueError:
            logger.error(f"Invalid number input: {args}")
            print(f"Invalid number input: {args[0]} or {args[1]} is not a valid number.")