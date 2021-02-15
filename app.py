from flask import Flask
from dotenv import load_dotenv, dotenv_values
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


def create_db(c_app):
    
    cdb = SQLAlchemy(c_app)
    cdb.create_all()
    return cdb

 
def create_app():
    flask_app = Flask(__name__)
    load_dotenv()
    flask_app.config.update(dotenv_values())
    return flask_app

app = create_app() 
db = create_db(app)
migrate = Migrate(app, db)
from apps.models.users import Users

from flasgger import Swagger
swagger = Swagger(app)
