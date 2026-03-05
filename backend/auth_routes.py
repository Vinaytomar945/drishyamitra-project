from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint("auth", __name__)

# Dummy user store (replace with DB later)
users = {"test": "password123"}

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = password
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if users.get(username) != password:
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=username)
    return jsonify({"access_token": token})

@auth_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify({"message": f"Hello {current_user}, you are authorized!"})
