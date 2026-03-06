from flask import Blueprint, request, jsonify
from models import Photo, FaceEmbedding
from database import db
from face_service import analyze_face, get_face_embedding, find_matching_face
import os, uuid, json

photo_bp = Blueprint("photo", __name__)

UPLOAD_FOLDER = "uploads"

@photo_bp.route("/upload", methods=["POST"])
def upload_photo():

    if "photo" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["photo"]

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    filename = str(uuid.uuid4()) + "_" + file.filename
    path = os.path.join(UPLOAD_FOLDER, filename)

    file.save(path)

    # analyze face
    analysis = analyze_face(path)

    # generate embedding
    embedding = get_face_embedding(path)

    # check if this face already exists
    match_photo_id = find_matching_face(embedding)

    photo = Photo(
        filename=filename,
        path=path
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

# from flask import Blueprint, request, jsonify
# from face_service import analyze_face, get_face_embedding
# from models import Photo, FaceEmbedding
# from database import db
# import os
# import uuid
# import json

# photo_bp = Blueprint("photo", __name__)

# UPLOAD_FOLDER = "uploads"

# @photo_bp.route("/upload", methods=["POST"])
# def upload_photo():

#     if "photo" not in request.files:
#         return jsonify({"error": "No file uploaded"}), 400

#     file = request.files["photo"]

#     os.makedirs(UPLOAD_FOLDER, exist_ok=True)

#     filename = str(uuid.uuid4()) + "_" + file.filename
#     path = os.path.join(UPLOAD_FOLDER, filename)

#     file.save(path)

#     # analyze face
#     analysis = analyze_face(path)

#     # generate embedding
#     embedding = get_face_embedding(path)

#     # store photo
#     photo = Photo(filename=filename, path=path)
#     db.session.add(photo)
#     db.session.commit()

#     # store embedding
#     face = FaceEmbedding(
#         photo_id=photo.id,
#         embedding=json.dumps(embedding)
#     )

#     db.session.add(face)
#     db.session.commit()

#     return jsonify({
#         "message": "Photo uploaded and processed",
#         "analysis": analysis
#     })