from flask import Blueprint, request, jsonify
import os
from werkzeug.utils import secure_filename

photo_bp = Blueprint("photos", __name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@photo_bp.route("/upload", methods=["POST"])
def upload_photo():
    if "photo" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["photo"]
    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    return jsonify({"message": "Photo uploaded successfully", "file_path": file_path})

@photo_bp.route("/list", methods=["GET"])
def list_photos():
    files = os.listdir(UPLOAD_FOLDER)
    return jsonify({"photos": files})
