from flask import Flask
from config import Configuration
from flask_restful import Resource, Api

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)
api = Api(app)

migrate=Migrate(app,db)
manager=Manager(app)

manager.add_command('db',MigrateCommand)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/rest1')
