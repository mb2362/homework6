import logging
from decimal import Decimal
from typing import Callable, List
from calculator.calculation import Calculation

# Configure logger
logger = logging.getLogger(__name__)

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """Add a new calculation to the history."""
        cls.history.append(calculation)
        logger.info(f"Added calculation: {calculation}")

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Retrieve the entire history of calculations."""
        logger.info(f"Retrieving calculation history. Total history count: {len(cls.history)}")
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clear the history of calculations."""
        cls.history.clear()
        logger.info("Cleared all calculation history.")

    @classmethod
    def get_latest(cls) -> Calculation:
        """Get the latest calculation. Returns None if there's no history."""
        if cls.history:
            logger.info(f"Latest calculation retrieved: {cls.history[-1]}")
            return cls.history[-1]
        logger.warning("No calculations in history to retrieve.")
        return None

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """Find and return a list of calculations by operation name."""
        found_calculations = [calc for calc in cls.history if calc.operation.__name__ == operation_name]
        logger.info(f"Found {len(found_calculations)} calculations with operation '{operation_name}'.")
        return found_calculations