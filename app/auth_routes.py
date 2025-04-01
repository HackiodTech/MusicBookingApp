from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models import db, User
from datetime import datetime
from app.extensions import db
from sqlalchemy.exc import IntegrityError

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    username = data.get("username")
    
    if not email or not password or not username:
        return jsonify({"message": "Email, password, and username are required."}), 400

    # Check if user already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"message": "User already exists."}), 400

    try:
        user = User(email=email, username=username, role=data.get("role", "user"))
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return jsonify({"data": {"message": "User successfully registered"}}), 201
    except IntegrityError as e:
        db.session.rollback()
        return jsonify({"data": {"message": "Failed to register user"}}), 500

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data["email"]).first()

    if user and user.check_password(data["password"]):
        token = create_access_token(identity=str(user.id)) 
        return jsonify({
            "data": {
                "token": token,
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "role": user.role
                }
            }
        })
    return jsonify({"data": {"error": "Invalid credentials"}}), 401

@auth_bp.route("/test", methods=["GET"])
def test_route():
    return jsonify({"data": {"message": "Blueprint works!"}}), 200
