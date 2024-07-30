
# Initializes the Flask app and registers blueprints.

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize the database
db = SQLAlchemy()

# Initiliaze the login manager
login_manager = LoginManager()


def create_app():
    # Create a new Flask application instance
    app = Flask(__name__)

    # Apply the configuration
    app.config.from_object(Config)

    # Initialize the database with the app
    db.init_app(app)

    # initialize the login manager with the map
    login_manager.init_app(app)

    # Import the routes module
    from . import routes

    # Register the blueprint from routes.py with the Flask application
    app.register_blueprint(routes.bp)

    # Return the Flask application instance
    return app

from .models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

