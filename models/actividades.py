import app


class Actividades(app.db.Model):
    actividadID = app.db.Column(app.db.Integer, primary_key=True)
    actividad = app.db.Column(app.db.String(100))
    responsableID = app.db.Column(app.db.Integer)
    dias = app.db.Column(app.db.String(100))
    horario = app.db.Column(app.db.String(100))
    asistentesMax = app.db.Column(app.db.Integer)

    def __init__(self, actividad, responsableID, dias, horario, asistentesMax):
        self.actividad = actividad
        self.responsableID = responsableID
        self.dias = dias
        self.horario = horario
        self.asistentesMax = asistentesMax
