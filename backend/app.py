import os
import json
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from deepface import DeepFace
from werkzeug.utils import secure_filename
from PIL import Image

from database import db
from models import User, Photo, FaceEmbedding
from auth_routes import auth_bp
from photo_routes import photo_bp
from face_routes import face_bp
from chat_routes import chat_bp
from email_routes import email_bp
# from whatsapp_routes import whatsapp_bp

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["TF_NUM_INTRAOP_THREADS"] = "1"
os.environ["TF_NUM_INTEROP_THREADS"] = "1"

# =============================
# LOAD ENVIRONMENT VARIABLES
# =============================
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

load_dotenv(os.path.join(ROOT_DIR, ".env"))

# =============================
# FLASK APP INIT
# =============================
app = Flask(__name__)
CORS(app)

# =============================
# CONFIGURATION
# =============================
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "sqlite:///" + os.path.join(BASE_DIR, "drishyamitra.db")
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["UPLOAD_FOLDER"] = os.path.join(BASE_DIR, "uploads")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "super-secret")

os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

db.init_app(app)
jwt = JWTManager(app)

with app.app_context():
    db.create_all()

# =============================
# HELPER FUNCTION
# =============================
def convert_numpy(obj):
    if hasattr(obj, "item"):
        return obj.item()
    if isinstance(obj, dict):
        return {k: convert_numpy(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [convert_numpy(i) for i in obj]
    return obj

# =============================
# BASIC ROUTES
# =============================
@app.route("/")
def home():
    return jsonify({"message": "DrishyaMitra backend running successfully"})

# =============================
# SERVE UPLOADED IMAGES
# =============================
@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

# =============================
# PHOTO GALLERY API
# =============================
@app.route("/photos", methods=["GET"])
def get_photos():

    photos = Photo.query.all()

    result = []

    for photo in photos:
        result.append({
            "id": photo.id,
            "filename": photo.filename,
            "person_name": photo.person_name,
            "image_url": f"/uploads/{photo.filename}",
            "age": photo.age,
            "gender": photo.gender
        })

    return jsonify(result)

# =============================
# REGISTER BLUEPRINTS
# =============================
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(photo_bp, url_prefix="/photo")
app.register_blueprint(face_bp, url_prefix="/face")
app.register_blueprint(chat_bp, url_prefix="/chat")
app.register_blueprint(email_bp, url_prefix="/email")
# app.register_blueprint(whatsapp_bp, url_prefix="/whatsapp")

