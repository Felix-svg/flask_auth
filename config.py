from flask import Flask
from sqlalchemy import MetaData
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager

app = Flask(__name__)
CORS(app, origins="*")
bcrypt = Bcrypt(app)

app.config['JWT_SECRET_KEY'] = "dsjkdfiwsnsdddfdjdssbohjoiaavg"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)
migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)
jwt = JWTManager(app)



