from flask import Blueprint, request, jsonify
from deepface import DeepFace

face_bp = Blueprint("face", __name__)

@face_bp.route("/detect", methods=["POST"])
def detect_face():
    try:
        if "photo" not in request.files:
            return jsonify({"error": "No file provided"}), 400

        file = request.files["photo"]
        file_path = "temp.jpg"
        file.save(file_path)

        analysis = DeepFace.analyze(
            img_path=file_path,
            actions=["age", "gender", "emotion"],
            enforce_detection=False,
            detector_backend="retinaface"
        )

        if isinstance(analysis, list):
            analysis = analysis[0]

        return jsonify(analysis)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
