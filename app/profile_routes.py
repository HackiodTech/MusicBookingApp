from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User
from app import db
from werkzeug.security import generate_password_hash

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/profile", methods=["GET"])
@jwt_required()
def view_profile():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    
    return jsonify({
        "id": user.id,
        "email": user.email,
        "role": user.role,
        "created_at": user.created_at
    })

@profile_bp.route("/profile", methods=["PUT"])
@jwt_required()
def edit_profile():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)

    data = request.get_json()
    new_email = data.get("email")
    new_password = data.get("password")

    if new_email:
        user.email = new_email

    if new_password:
        user.password_hash = generate_password_hash(new_password)

    db.session.commit()

    return jsonify({
        "message": "Profile updated successfully",
        "user": {
            "id": user.id,
            "email": user.email,
            "role": user.role
        }
    })