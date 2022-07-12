import app
from flask_login import UserMixin


class Usuarios(UserMixin, app.db.Model):
    id = app.db.Column(app.db.Integer, primary_key=True)
    usuario = app.db.Column(app.db.String(100))
    clave = app.db.Column(app.db.String(100))
    # rol = db.column(db.String(100))
    nombre = app.db.Column(app.db.String(100))
    # apellido = db.column(db.String(100))

    # def __init__(self, usuario, clave, rol, nombre, apellido):
    #     self.usuario = usuario
    #     self.clave = clave
    #     self.rol = rol
    #     self.nombre = nombre
    #     self.apellido = apellido
    #
    # def __init__(self, usuario, clave):
    #     self.usuario = usuario
    #     self.clave = clave