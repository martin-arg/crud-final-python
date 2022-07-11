from app import db,ma


class Usuarios(db.Model):
    usuarioID = db.column(db.Integer, primary_key=True)
    usuario = db.column(db.String(100))
    clave = db.column(db.String(100))
    rol = db.column(db.String(100))
    nombre = db.column(db.String(100))
    apellido = db.column(db.String(100))

    def __init__(self, usuario, clave, rol, nombre, apellido):
        self.usuario = usuario
        self.clave = clave
        self.rol = rol
        self.nombre = nombre
        self.apellido = apellido

    def __init__(self, usuario, clave):
        self.usuario = usuario
        self.clave = clave