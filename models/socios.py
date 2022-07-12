import app


class Socios(app.db.Model):
    socioID = app.db.Column(app.db.Integer, primary_key = True)
    name = app.db.Column(app.db.String(100))
    dni = app.db.Column(app.db.Integer)
    email = app.db.Column(app.db.String(100))

    def __init__(self, name, dni, email):
        self.name = name
        self.dni = dni
        self.email = email


