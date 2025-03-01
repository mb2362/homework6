import importlib
import os
from app.commands import CommandHandler

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
                module = importlib.import_module(f"{module_name}")  # Import dynamically
                command_class_name = f"{folder}Command"  # Expected class name (e.g., addCommand)
                command_class = getattr(module, command_class_name, None)  # Get class dynamically

                if command_class:
                    command_handler.register_command(folder, command_class())  # Register command
                else:
                    print(f"⚠ Warning: {command_class_name} not found in {module_name}")
            except Exception as e:
                print(f"❌ Error loading plugin {module_name}: {e}")

    return command_handler  # Return populated command handler
