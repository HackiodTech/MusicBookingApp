# app/__init__.py
from flask import Flask
from dotenv import load_dotenv
from config import Config
import os

# Load environment variables
load_dotenv()

from app.extensions import db, migrate, jwt

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(Config)
    # Alternatively:
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Youngboy1@localhost/music_booking_db'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    # Import models so that they are registered with db.metadata
    from app import models  # This will import models.py

    # Register blueprints
    from app.routes import api
    app.register_blueprint(api, url_prefix="/api")

    return app
