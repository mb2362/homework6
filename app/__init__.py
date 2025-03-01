# APP
from app.plugins.plugins_manager import load_plugins

class App:
    def __init__(self):
        self.command_handler = load_plugins()  # Load plugins dynamically

    def start(self):
        """Runs the command loop to process user input."""
        print("Type 'exit' to exit or 'menu' to enter the menu section.")
        while True:
            cmd_input = input(">>> ").strip().split()
            if not cmd_input:
                continue

            cmd_name = cmd_input[0].lower()
            args = cmd_input[1:]

            if cmd_name in self.command_handler.commands:
                try:
                    self.command_handler.commands[cmd_name].execute(args)
                except Exception as e:
                    print(f"Error executing command '{cmd_name}': {e}")
            elif cmd_name == "exit":
                print("Exiting application...")
                break
            else:
                print(f"No such command: {cmd_name}")