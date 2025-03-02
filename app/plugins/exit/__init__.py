# EXIT
import logging
from app.commands import CLI
import sys

# Configure logger
logger = logging.getLogger(__name__)

class exitCommand(CLI):
    def execute(self, args):
        # Log the exit action
        logger.info("Exiting application...")

        print("Exiting...")
        sys.exit("Exiting...")