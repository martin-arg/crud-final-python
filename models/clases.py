import app


class Clases(app.db.Model):
    actividadID = app.db.Column(app.db.Integer, primary_key=True)
    socioID = app.db.Column(app.db.Integer, primary_key=True)

    def __init__(self, actividadID, socioID):
        self.actividadID = actividadID
        self.socioID = socioID
