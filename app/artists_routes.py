from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, Artist, User

artist_bp = Blueprint("artist", __name__)

@artist_bp.route("/", methods=["POST"])
@jwt_required()
def create_artist_profile():
    current_user = User.query.get(get_jwt_identity())
    data = request.get_json()
    artist = Artist(
        user_id=current_user.id,
        stage_name=data["stage_name"],
        bio=data.get("bio"),
        genre=data.get("genre"),
    )
    db.session.add(artist)
    db.session.commit()
    return jsonify({"message": "Artist profile created"}), 201
