from app import app
from flask import render_template


@app.route('/')
def index():
    name = 'ivan'
    print("path sql", app.config['SQLALCHEMY_DATABASE_URI'])
    return render_template('index.html', n=name)
