from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User, Artist, Event, Booking
from app.extensions import db

bookings_bp = Blueprint("bookings", __name__)

@bookings_bp.route("/book_event", methods=["POST"])
@jwt_required()
def book_event():
    user_id = get_jwt_identity()
    data = request.get_json()

    event_id = data.get("event_id")
    tickets = data.get("tickets")

    if not tickets or tickets <= 0:
        return jsonify({"message": "Invalid number of tickets"}), 400

    event = Event.query.get(event_id)
    if not event or event.tickets_available < tickets:
        return jsonify({"message": "Event not available or insufficient tickets"}), 400

    # Create booking
    total_price = event.price * tickets
    booking = Booking(
        user_id=user_id,
        event_id=event_id,
        tickets=tickets,
        total_price=total_price
    )

    event.tickets_available -= tickets

    db.session.add(booking)
    db.session.commit()

    return jsonify({
        "message": "Booking successful",
        "booking_id": booking.id,
        "event": {
            "id": event.id,
            "title": event.title,
            "date_time": event.date_time
        },
        "tickets": tickets,
        "total_price": total_price
    })

@bookings_bp.route("/book_artist", methods=["POST"])
@jwt_required()
def book_artist():
    # Get the user making the request
    user_id = get_jwt_identity()

    data = request.get_json()

    event_id = data.get("event_id")
    artist_id = data.get("artist_id")

    # Find the event and artist
    event = Event.query.get(event_id)
    artist = Artist.query.get(artist_id)

    if not event:
        return jsonify({"error": "Event not found"}), 404

    if not artist:
        return jsonify({"error": "Artist not found"}), 404

    # Check if the event is already booked with an artist
    if event.artist_id:
        return jsonify({"error": "Event already has an artist booked"}), 400

    # Assign artist to the event
    event.artist_id = artist.id

    # Commit the change
    db.session.commit()

    return jsonify({
        "message": "Artist successfully booked for the event",
        "event": {
            "id": event.id,
            "title": event.title,
            "artist": {
                "id": artist.id,
                "stage_name": artist.stage_name,
                "bio": artist.bio,
                "genre": artist.genre
            }
        }
    })
