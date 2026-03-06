from database import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# -------------------------
# User Model
# -------------------------
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    # Relationships
    photos = db.relationship("Photo", backref="user", lazy=True)
    deliveries = db.relationship("DeliveryHistory", backref="user", lazy=True)

    # Utility methods for password hashing
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# -------------------------
# Photo Model
# -------------------------
class Photo(db.Model):
    __tablename__ = "photos"

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), nullable=False)
    person_name = db.Column(db.String(100))
    path = db.Column(db.String(300), nullable=False)

    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)   # photo upload time
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))      # link to User table
    age = db.Column(db.Integer)                                     # detected age
    gender = db.Column(db.String(20))                               # detected gender

    # Relationships
    faces = db.relationship("Face", backref="photo", lazy=True)


# -------------------------
# Face Model
# -------------------------
class FaceEmbedding(db.Model):
    __tablename__ = "face_embeddings"

    id = db.Column(db.Integer, primary_key=True)

    photo_id = db.Column(db.Integer, db.ForeignKey('photos.id'))

    embedding = db.Column(db.Text)
    
class Face(db.Model):
    __tablename__ = "faces"

    id = db.Column(db.Integer, primary_key=True)
    photo_id = db.Column(db.Integer, db.ForeignKey("photos.id"), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey("persons.id"))  # link to Person table

    encoding = db.Column(db.Text)   # face embedding/encoding
    age = db.Column(db.Integer)
    gender = db.Column(db.String(20))


# -------------------------
# Person Model
# -------------------------
class Person(db.Model):
    __tablename__ = "persons"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(20))

    # Relationship: One person can have many faces
    faces = db.relationship("Face", backref="person", lazy=True)


# -------------------------
# DeliveryHistory Model
# -------------------------
class DeliveryHistory(db.Model):
    __tablename__ = "delivery_history"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    delivery_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), nullable=False)


