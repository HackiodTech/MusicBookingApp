import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    
    # Ensure DATABASE_URL is picked up
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Youngboy1@localhost/music_booking_db'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_jwt_secret")
