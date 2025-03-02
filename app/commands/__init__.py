#  Commands
import logging
from abc import ABC, abstractmethod

# Configure logger
logger = logging.getLogger(__name__)

class CLI(ABC):
    @abstractmethod
    def execute(self, args):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}
        logger.info("CommandHandler initialized.")

    def register_command(self, command_name: str, command: CLI):
        self.commands[command_name] = command
        logger.info(f"Command registered: {command_name}")

    def execute_command(self, command_name: str):
        try:
            logger.info(f"Executing command: {command_name}")
            self.commands[command_name].execute([])
        except KeyError:
            logger.warning(f"No such command: {command_name}")
            print(f"No such command: {command_name}")