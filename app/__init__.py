# APP
import logging
import logging.config
import os
from dotenv import load_dotenv
from app.plugins.plugins_manager import load_plugins

# Define log directory and config path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Project root
LOG_CONFIG_PATH = os.path.join(BASE_DIR, "logging.conf")
LOG_DIR = os.path.join(BASE_DIR, "logs")

# Ensure log directory exists
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)  # Create the logs directory if it doesn't exist

# Load logging configuration
if os.path.exists(LOG_CONFIG_PATH):
    logging.config.fileConfig(LOG_CONFIG_PATH)
else:
    logging.basicConfig(level=logging.INFO)  # Fallback in case logging.conf is missing
    logging.warning(f"Logging configuration file '{LOG_CONFIG_PATH}' not found. Using default settings.")

logger = logging.getLogger(__name__)
logger.info("Logging is successfully set up.")

class App:
    def __init__(self):
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        logger.info("Initializing application and loading plugins.")
        self.command_handler = load_plugins()  # Load plugins dynamically

    def load_environment_variables(self):
        """
        Loads all environment variables into a dictionary.
        Iterates through os.environ.items() and stores each key-value pair in the 'settings' dictionary.
        Logs a message indicating that the environment variables have been loaded.
        
        Returns:
            dict: A dictionary containing all environment variables.
        """
        settings = {key: value for key, value in os.environ.items()}  # Create a dictionary with environment variables
        logging.info("Environment variables loaded.")  # Log the loading process
        return settings  # Return the dictionary with environment variables

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        """
        Retrieves the value of a specific environment variable.
        If the variable is not found, it returns None.

        Args:
            env_var (str): The name of the environment variable to retrieve. Defaults to 'ENVIRONMENT'.
            
        Returns:
            str or None: The value of the environment variable or None if not found.
        """
        return self.settings.get(env_var, None)  # Return the value of the requested environment variable or None


    def start(self):
        """Runs the command loop to process user input."""
        logger.info("Application started. Waiting for user input.")
        print("Type 'exit' to exit or 'menu' to enter the menu section.")
        
        while True:
            cmd_input = input(">>> ").strip().split()
            if not cmd_input:
                continue

            cmd_name = cmd_input[0].lower()
            args = cmd_input[1:]
            logger.info(f"User input received: {cmd_name} {args}")

            if cmd_name in self.command_handler.commands:
                try:
                    logger.info(f"Executing command: {cmd_name}")
                    self.command_handler.commands[cmd_name].execute(args)
                except Exception as e:
                    logger.error(f"Error executing command '{cmd_name}': {e}", exc_info=True)
                    print(f"Error executing command '{cmd_name}': {e}")
            elif cmd_name == "exit":
                logger.info("Exiting application.")
                print("Exiting application...")
                break
            else:
                logger.warning(f"Unknown command: {cmd_name}")
                print(f"No such command: {cmd_name}")