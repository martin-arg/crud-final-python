from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from routes.routes import routes

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+pymysql://root@localhost/clubsocial'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(routes)
db = SQLAlchemy(app)
ma = Marshmallow(app)
