import logging
from decimal import Decimal

# Configure logger
logger = logging.getLogger(__name__)

# Define the functions with type hints and logging

def add(a: Decimal, b: Decimal) -> Decimal:
    result = a + b
    logger.info(f"Performed addition: {a} + {b} = {result}")
    return result

def subtract(a: Decimal, b: Decimal) -> Decimal:
    result = a - b
    logger.info(f"Performed subtraction: {a} - {b} = {result}")
    return result

def multiply(a: Decimal, b: Decimal) -> Decimal:
    result = a * b
    logger.info(f"Performed multiplication: {a} * {b} = {result}")
    return result

def divide(a: Decimal, b: Decimal) -> Decimal:
    try:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        logger.info(f"Performed division: {a} / {b} = {result}")
        return result
    except ValueError as e:
        logger.error(f"Error in division: {e} - operands were {a} and {b}")
        raise  # Re-raise the exception after logging
