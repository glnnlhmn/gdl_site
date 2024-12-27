import pytest
from app import create_app
from config import TestingConfig

@pytest.mark.usefixtures("app")
def test_app_creation():
    app = create_app(TestingConfig)
    assert app is not None
    assert app.config['TESTING'] is True

@pytest.mark.usefixtures("app")
def test_blueprint_registration():
    app = create_app(TestingConfig)
    assert 'main' in app.blueprints

@pytest.mark.usefixtures("app")
def test_app_configuration():
    app = create_app(TestingConfig)
    assert app.config['DEBUG'] is False  # Assuming TestingConfig sets DEBUG to False
    assert app.config['TESTING'] is True