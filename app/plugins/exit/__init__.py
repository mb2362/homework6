# EXIT
from app.commands import CLI
import sys

class exitCommand(CLI):
    def execute(self, args):
        print("Exiting...")
        sys.exit("Exiting...")