from deepface import DeepFace
import numpy as np
import os
import json
from models import FaceEmbedding
from database import db

def analyze_face(image_path):
    try:
        result = DeepFace.analyze(
            img_path=image_path,
            actions=["age", "gender", "emotion"],
            enforce_detection=False,
            detector_backend="opencv"
        )

        if isinstance(result, list):
            result = result[0]

        return {
            "age": int(result.get("age")),
            "gender": result.get("dominant_gender"),
            "emotion": result.get("dominant_emotion")
        }

    except Exception as e:
        return {"error": str(e)}


def get_face_embedding(image_path):
    """
    Generate face embedding using Facenet512 model
    """

    embedding = DeepFace.represent(
        img_path=image_path,
        model_name="Facenet512",
        enforce_detection=False
    )

    if isinstance(embedding, list):
        embedding = embedding[0]

    return embedding["embedding"]

def find_matching_face(new_embedding, threshold=0.9):

    faces = FaceEmbedding.query.all()

    for face in faces:
        stored_embedding = json.loads(face.embedding)

        distance = np.linalg.norm(
            np.array(new_embedding) - np.array(stored_embedding)
        )

        if distance < threshold:
            return face.photo_id

    return None