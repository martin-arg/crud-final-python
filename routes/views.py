from flask import Blueprint, render_template, request
from models.usuarios import Usuarios

views = Blueprint('views', __name__)


@views.route("/loguear", methods=['POST'])
def login():
    usuario = request.form['usuario']
    password = request.form['password']

    new_Usuarios(usuario, password)

    print(new_Usuarios)
    return render_template('./views/logueado.html')
