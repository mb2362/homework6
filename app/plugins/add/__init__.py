# ADDITION
import logging
from app.commands import CLI
from calculator import Calculator

# Configure logger
logger = logging.getLogger(__name__)

class addCommand(CLI):
    def execute(self, args):
        if len(args) != 2:
            logger.warning("Invalid arguments for add command. Expected 2 arguments.")
            print("Usage: add <a> <b>")
            return
        try:
            a = float(args[0])
            b = float(args[1])
            result = Calculator.add(a, b)
            logger.info(f"Addition executed: {a} + {b} = {result}")
            print(f"The result of {int(a)} + {int(b)} is equal to {result}")
        except ValueError:
            logger.error(f"Invalid number input: {args}")
            print(f"Invalid number input: {args[0]} or {args[1]} is not a valid number.")