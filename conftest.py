import pytest
from app import create_app
from config import TestingConfig
from tests.test_routes import test_blueprint

# Fixture to create and configure the Flask app for testing
@pytest.fixture
def app():
    # Create an instance of the app with the testing configuration
    app = create_app(config_class=TestingConfig)
    # Enable testing mode
    app.config['TESTING'] = True

    # Push the application context to make the app ready for testing
    with app.app_context():
        # Yield the app instance to be used in tests
        yield app

# Fixture to create a test client for making HTTP requests to the app
@pytest.fixture
def client(app):
    # Return the test client for the app
    return app.test_client()

# Fixture to create a CLI runner for invoking command-line commands
@pytest.fixture
def runner(app):
    # Return the CLI runner for the app
    return app.test_cli_runner()

    # This approach is used to allow for invoking CLI commands in the future.
    # By setting up the `runner` fixture, we ensure that we can easily test
    # any custom Flask CLI commands we might add to our application later on.
    # This makes our test setup more flexible and extensible, accommodating
    # future needs without requiring significant changes to our test configuration.