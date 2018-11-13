from flask import Flask
from config import Configuration
from flask_restful import Resource, Api

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
api = Api(app)

db = SQLAlchemy(app)
app.config.from_object(Configuration)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/rest1')



