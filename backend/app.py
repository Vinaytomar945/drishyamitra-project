import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from database import db
from models import Photo
from face_service import analyze_face
from chat_service import chat_with_ai

UPLOAD_FOLDER = "uploads"

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///instance/drishyamitra.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return {"message": "Backend running successfully"}

@app.route("/upload", methods=["POST"])
def upload_photo():
    file = request.files["photo"]

    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    analysis = analyze_face(path)

    photo = Photo(filename=file.filename, person_name="Unknown", path=path)
    db.session.add(photo)
    db.session.commit()

    return jsonify({
        "message": "Uploaded",
        "analysis": analysis
    })


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    msg = data.get("message")

    reply = chat_with_ai(msg)

    return {"response": reply}


if __name__ == "__main__":
    app.run(debug=True)