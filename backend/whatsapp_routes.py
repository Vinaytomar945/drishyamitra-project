from flask import Blueprint, request, jsonify
from whatsapp_service import send_photo_whatsapp

whatsapp_bp = Blueprint("whatsapp", __name__)

@whatsapp_bp.route("/send-photo", methods=["POST"])
def send_whatsapp():

    data = request.json

    phone = data.get("phone")
    photo = data.get("photo_path")

    if not phone or not photo:
        return jsonify({"error": "phone and photo_path required"}), 400

    result = send_photo_whatsapp(phone, photo)

    return jsonify({"message": result})