from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from routes.principal import principal
from routes.views import views

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+pymysql://root@localhost/clubsocial'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(principal)
app.register_blueprint(views)
db = SQLAlchemy(app)
ma = Marshmallow(app)
