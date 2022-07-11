from app import db, ma


class Actividades(db.Model):
    actividadID = db.Column(db.Integer, primary_key=True)
    actividad = db.Column(db.String(100))
    responsableID = db.Column(db.Integer)
    dias = db.Column(db.String(100))
    horario = db.Column(db.String(100))
    asistentesMax = db.Column(db.Integer)

    def __init__(self, actividad, responsableID, dias, horario, asistentesMax):
        self.actividad = actividad
        self.responsableID = responsableID
        self.dias = dias
        self.horario = horario
        self.asistentesMax = asistentesMax
