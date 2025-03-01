#  Commands
from abc import ABC, abstractmethod

class CLI(ABC):
    @abstractmethod
    def execute(self, args):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: CLI):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        try:
            self.commands[command_name].execute([])
        except KeyError:
            print(f"No such command: {command_name}")