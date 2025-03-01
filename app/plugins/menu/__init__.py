# MENU
from app.commands import CLI

class menuCommand(CLI):
    def execute(self, args):
        print("Available Commands:")
        print("- add <a> <b>: Perform addition")
        print("- subtract <a> <b>: Perform subtraction")
        print("- multiply <a> <b>: Perform multiplication")
        print("- divide <a> <b>: Perform division")
        print("- exit: Exit the application")
