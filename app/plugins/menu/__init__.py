# MENU
import logging
from app.commands import CLI

# Configure logger
logger = logging.getLogger(__name__)

class menuCommand(CLI):
    def execute(self, args):
        # Log the action of displaying the menu
        logger.info("Displaying available commands.")

        print("Available Commands:")
        print("- add <a> <b>: Perform addition")
        print("- subtract <a> <b>: Perform subtraction")
        print("- multiply <a> <b>: Perform multiplication")
        print("- divide <a> <b>: Perform division")
        print("- exit: Exit the application")