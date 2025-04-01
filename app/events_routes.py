from flask import Blueprint, jsonify, request
from datetime import datetime
from app.models import Artist, Event, User, db
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db

events_bp = Blueprint("events", __name__)

@events_bp.route("/events", methods=["GET"])
def view_events():
    events = Event.query.all()
    
    event_list = [{
        "id": event.id,
        "title": event.title,
        "description": event.description,
        "date_time": event.date_time,
        "price": event.price,
        "tickets_available": event.tickets_available,
        "artist": {
            "id": event.artist.id if event.artist else None,  # Check if artist exists
            "stage_name": event.artist.stage_name if event.artist else "No artist"  # Handle case where artist is None
        } if event.artist else {"id": None, "stage_name": "No artist"}  # If no artist, return default values
    } for event in events]
    
    return jsonify({"data": event_list})

@events_bp.route("/create", methods=["POST"])
@jwt_required()
def create_event():
    data = request.get_json()
    
    # Get current user's ID
    user_id = get_jwt_identity()  # Get the current logged-in user's ID

    title = data.get("title")
    description = data.get("description")
    date_time = datetime.strptime(data.get("date_time"), "%Y-%m-%d %H:%M:%S")  # Convert string to datetime
    price = data.get("price")
    tickets_available = data.get("tickets_available")
    is_paid = data.get("is_paid", False)  # Whether the event is paid or not
    
    # Check if the event is paid and the price is provided
    if is_paid and not price:
        return jsonify({"data": {"message": "Price is required for paid events."}}), 400

    # Check if the user is an artist (optional step)
    artist = Artist.query.filter_by(user_id=user_id).first()  # Check if the user is an artist

    if artist:
        artist_id = artist.id  # If the user is an artist, link the event to their artist ID
    else:
        artist_id = None  # If the user is not an artist, leave artist_id as None
    
    # Create event and associate it with the user or artist
    event = Event(
        title=title,
        description=description,
        date_time=date_time,
        price=price if is_paid else None,  # Only add price if the event is paid
        tickets_available=tickets_available,
        artist_id=artist_id  # Link event to the artist or None if not an artist
    )

    try:
        db.session.add(event)
        db.session.commit()
        return jsonify({"data": {"message": "Event created successfully", "event_id": event.id}}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"data": {"error": str(e)}}), 500