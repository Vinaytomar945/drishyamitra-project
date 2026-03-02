import os
from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder="uploads")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///drishyamitra.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["UPLOAD_FOLDER"] = "uploads"

db = SQLAlchemy(app)
CORS(app)

# ==============================
# Database Models
# ==============================

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), nullable=False)
    prediction = db.Column(db.String(200), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))

    person = db.relationship('Person', backref=db.backref('images', lazy=True))

# Upload folder create karo
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# ==============================
# Routes
# ==============================

@app.route("/")
def home():
    return {"message": "Backend is running successfully!"}


@app.route("/send", methods=["POST"])
def receive_data():
    data = request.json
    name = data.get("name")
    return {"reply": f"Hello {name}, backend received your data!"}


@app.route("/add_person", methods=["POST"])
def add_person():
    name = request.json.get("name")

    new_person = Person(name=name)
    db.session.add(new_person)
    db.session.commit()

    return {"message": "Person added successfully"}


@app.route("/upload", methods=["POST"])
def upload_image():
    file = request.files.get("image")

    if not file:
        return {"message": "No file uploaded"}

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Fake AI logic
    if "cat" in file.filename.lower():
        prediction = "This looks like a Cat 🐱"
    elif "dog" in file.filename.lower():
        prediction = "This looks like a Dog 🐶"
    else:
        prediction = "Object detected successfully 🔍"

    # Save to database
    new_image = Image(filename=file.filename, prediction=prediction)
    db.session.add(new_image)
    db.session.commit()

    return {
        "message": f"Image saved as {file.filename}",
        "prediction": prediction
    }


@app.route("/images", methods=["GET"])
def get_images():
    images = Image.query.all()
    return [
        {
            "id": img.id,
            "filename": img.filename,
            "prediction": img.prediction
        }
        for img in images
    ]


@app.route("/uploads/<filename>")
def get_image(filename):
    return app.send_static_file(filename)


# Create tables
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)