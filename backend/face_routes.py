from flask import Blueprint, request, jsonify
from face_service import analyze_face
import os
import uuid

face_bp = Blueprint("face", __name__)

UPLOAD_FOLDER = "uploads"

@face_bp.route("/detect", methods=["POST"])
def detect_face():
    try:
        if "photo" not in request.files:
            return jsonify({"error": "No file provided"}), 400

        file = request.files["photo"]

        if file.filename == "":
            return jsonify({"error": "Empty filename"}), 400

        # Create uploads folder if not exists
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        # Unique filename to avoid overwrite
        filename = str(uuid.uuid4()) + "_" + file.filename
        file_path = os.path.join(UPLOAD_FOLDER, filename)

        # Save image
        file.save(file_path)

        # Call service layer
        analysis = analyze_face(file_path)

        return jsonify({
            "message": "Face analyzed successfully",
            "analysis": analysis,
            "image_path": file_path
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500