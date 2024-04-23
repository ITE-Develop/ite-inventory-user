import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

BASEDIR = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
from app.models import *

def create_app():
    
    app = Flask(__name__)
    # Load flask configuration
    config = Config()
    app.config.from_object(config)
    
    # Initialize database and CSRF protection
    db.init_app(app)
    
    return app