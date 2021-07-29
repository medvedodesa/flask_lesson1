from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    depart = db.Column(db.String(24))
    dol = db.Column(db.String(140))
