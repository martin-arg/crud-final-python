from app import db,ma


class Socios(db.Model):
    socioID = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    dni = db.Column(db.Integer)
    email = db.Column(db.String(100))

    def __init__(self, name, dni, email):
        self.name = name
        self.dni = dni
        self.email = email


