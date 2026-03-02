from database import db

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200))
    person_name = db.Column(db.String(100))
    path = db.Column(db.String(300))