"""Test for .env"""
import pytest  # pylint: disable=unused-import
from app import App

def test_app_get_environment_variable():
    """Test the 'get_environment_variable()' method of the App class."""
    app = App()
    # Retrieve the current environment setting
    current_env = app.get_environment_variable('ENVIRONMENT')
    # Assert that the current environment is what you expect
    assert current_env in ['DEVELOPMENT', 'TESTING', 'PRODUCTION'], f"Invalid ENVIRONMENT: {current_env}"
