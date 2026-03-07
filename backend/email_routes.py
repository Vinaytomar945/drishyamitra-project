from flask import Blueprint, request, jsonify
from email_service import send_photo_email

email_bp = Blueprint("email", __name__)

@email_bp.route("/send-photo", methods=["POST"])
def send_photo():

    data = request.json

    email = data.get("email")
    photo_path = data.get("photo_path")

    if not email or not photo_path:
        return jsonify({"error": "Email and photo_path required"}), 400

    result = send_photo_email(email, photo_path)

    return jsonify({"message": result})