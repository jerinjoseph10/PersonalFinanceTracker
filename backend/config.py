#Purpose: This file will hold the configuration settings for your Flask app, including the database URI.

import os


class Config:
    # Set the base directory for the project
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Configure the SQLite database URI
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret key for session management
    SECRET_KEY = 'your_secret_key_here'
