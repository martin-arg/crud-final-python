from app import db, ma


class Clases(db.Model):
    actividadID = db.Column(db.Integer, primary_key=True)
    socioID = db.Column(db.Integer, primary_key=True)

    def __init__(self, actividadID, socioID):
        self.actividadID = actividadID
        self.socioID = socioID
