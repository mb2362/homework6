# PLUGINS MANAGER
import importlib
import os
import logging
from app.commands import CommandHandler

# Configure logger
logger = logging.getLogger(__name__)

PLUGIN_FOLDER = "app.plugins"

def load_plugins():
    """Dynamically load all plugins from subdirectories within the plugins folder."""
    command_handler = CommandHandler()
    plugin_path = os.path.dirname(__file__)  # Get the path to the plugins directory

    for folder in os.listdir(plugin_path):
        plugin_dir = os.path.join(plugin_path, folder)
        
        # Ensure it's a directory and contains an __init__.py file (to be a valid package)
        if os.path.isdir(plugin_dir) and "__init__.py" in os.listdir(plugin_dir):
            module_name = f"{PLUGIN_FOLDER}.{folder}"  # Convert to module path
            
            try:
                # Attempt to dynamically import the module
                module = importlib.import_module(f"{module_name}")
                command_class_name = f"{folder}Command"  # Expected class name (e.g., addCommand)
                
                # Get the class dynamically
                command_class = getattr(module, command_class_name, None)

                if command_class:
                    # Register the command if the class is found
                    command_handler.register_command(folder, command_class())  
                    logger.info("Plugin loaded successfully: %s", module_name)
                else:
                    logger.warning("⚠ Warning: %s not found in %s", command_class_name, module_name)

            except Exception as e:
                # Log any exceptions that occur during the import or command registration
                logger.error("❌ Error loading plugin %s: %s", module_name, e)

    return command_handler  # Return populated command handler