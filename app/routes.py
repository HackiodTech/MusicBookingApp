from flask import Blueprint
api = Blueprint("api", __name__)

# Import routes to attach them to the blueprint
from app.auth_routes import auth_bp
from app.artists_routes import artist_bp
from app.profile_routes import profile_bp
from app.events_routes import events_bp
from app.booking_routes import bookings_bp

# Register individual route files
api.register_blueprint(auth_bp, url_prefix="/auth")
api.register_blueprint(artist_bp, url_prefix="/artists")
api.register_blueprint(profile_bp, url_prefix="/profile")
api.register_blueprint(events_bp, url_prefix="/events")
api.register_blueprint(bookings_bp, url_prefix="/bookings")
