import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from deepface import DeepFace

from database import db
from models import Photo

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# =============================
# CONFIGURATION
# =============================

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "sqlite:///" + os.path.join(BASE_DIR, "drishyamitra.db")
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["UPLOAD_FOLDER"] = os.path.join(BASE_DIR, "uploads")

# Ensure upload folder exists
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

db.init_app(app)

with app.app_context():
    db.create_all()

# =============================
# HELPER FUNCTION
# =============================

def convert_numpy(obj):
    """
    Recursively convert numpy types to Python native types
    so Flask can jsonify them.
    """
    if hasattr(obj, "item"):
        return obj.item()
    if isinstance(obj, dict):
        return {k: convert_numpy(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [convert_numpy(i) for i in obj]
    return obj

# =============================
# ROUTES
# =============================

@app.route("/")
def home():
    return jsonify({"message": "Backend running successfully"})

@app.route("/upload", methods=["POST"])
def upload_photo():
    try:
        if "photo" not in request.files:
            return jsonify({"error": "No file provided"}), 400

        file = request.files["photo"]

        if file.filename == "":
            return jsonify({"error": "Empty filename"}), 400

        # Save file
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)

        # Analyze face
        analysis = DeepFace.analyze(
            img_path=file_path,
            actions=["age", "gender"],
            enforce_detection=False
        )

        # DeepFace sometimes returns list
        if isinstance(analysis, list):
            analysis = analysis[0]

        # Convert numpy values
        analysis = convert_numpy(analysis)

        age = analysis.get("age")
        gender = analysis.get("dominant_gender")

        # Save to DB
        photo = Photo(
            filename=file.filename,
            person_name="Unknown",
            path=file_path,
            age=age,
            gender=gender
        )

        db.session.add(photo)
        db.session.commit()

        return jsonify({
            "message": "Uploaded successfully",
            "age": age,
            "gender": gender,
            "image_url": f"/uploads/{file.filename}"   # ✅ Added image URL
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/photos", methods=["GET"])
def get_photos():
    photos = Photo.query.all()

    result = []
    for photo in photos:
        result.append({
            "id": photo.id,
            "filename": photo.filename,
            "person_name": photo.person_name,
            "path": photo.path,
            "age": photo.age,
            "gender": photo.gender
        })

    return jsonify(result)


# =============================
# START SERVER
# =============================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
