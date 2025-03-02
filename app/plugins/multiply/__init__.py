# MULTIPLICATION
import logging
from app.commands import CLI
from app.commands import CLI
from calculator import Calculator

# Configure logger
logger = logging.getLogger(__name__)

class multiplyCommand(CLI):
    def execute(self, args):
        # Log the attempt to execute multiplication
        logger.info("Executing multiplication command with arguments: %s", args)
        
        if len(args) != 2:
            print("Usage: multiply <a> <b>")
            logger.warning("Invalid number of arguments. Expected 2 arguments, but got %d.", len(args))
            return

        try:
            a = float(args[0])
            b = float(args[1])
            result = Calculator.multiply(a, b)
            print(f"The result of {int(a)} x {int(b)} is equal to {result}")
            logger.info("Multiplication successful: %f x %f = %f", a, b, result)
        except ValueError:
            print(f"Invalid number input: {args[0]} or {args[1]} is not a valid number.")
            logger.error("ValueError: Invalid number input. Args: %s", args)
        except ZeroDivisionError:
            print("An error occurred: Cannot divide by zero.")
            logger.error("ZeroDivisionError: Tried to divide by zero. Args: %s", args)