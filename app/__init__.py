# app/__init__.py

from flask import Flask
from config import Config, DevelopmentConfig, TestingConfig, ProductionConfig

__version__ = "0.2.0"

def create_app(config_class=Config):
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config_class)

    # Register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app