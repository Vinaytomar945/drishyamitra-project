from flask import Blueprint, request, jsonify
from models import Photo, FaceEmbedding
from database import db
from face_service import analyze_face, get_face_embedding, find_matching_face
import os, uuid, json
from flask import send_from_directory

photo_bp = Blueprint("photo", __name__)

UPLOAD_FOLDER = "uploads"

@photo_bp.route("/upload", methods=["POST"])
def upload_photo():

    if "photo" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["photo"]

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    filename = str(uuid.uuid4()) + "_" + file.filename
    path = f"{UPLOAD_FOLDER}/{filename}"

    file.save(path)

    # analyze face
    analysis = analyze_face(path)

    age = analysis.get("age")
    gender = analysis.get("dominant_gender")

    # generate embedding
    embedding = get_face_embedding(path)

    # check if face already exists
    match_photo_id = find_matching_face(embedding)

    photo = Photo(
        filename=filename,
        path=path,
        age=age,
        gender=gender
    )

    db.session.add(photo)
    db.session.commit()

    # store embedding
    face = FaceEmbedding(
        photo_id=photo.id,
        embedding=json.dumps(embedding)
    )

    db.session.add(face)
    db.session.commit()

    return jsonify({
        "message": "Photo uploaded and processed",
        "analysis": analysis,
        "matched_photo_id": match_photo_id
    })

@photo_bp.route("/uploads/<filename>")
def get_uploaded_photo(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@photo_bp.route("/list", methods=["GET"])
def list_photos():

    photos = Photo.query.all()

    result = []

    for photo in photos:
        result.append({
            "id": photo.id,
            "filename": photo.filename,
            "image_url": f"/uploads/{photo.filename}",
            "age": photo.age,
            "gender": photo.gender
        })

    return jsonify(result)