#!/usr/bin/env python3

from flask import Flask, make_response,jsonify
from flask_migrate import Migrate

from models import db, Hero

import os

abs_path=os.getcwd()

abs_python_path=os.path.normpath(abs_path)
db_path=f'sqlite:///{abs_path}/db/app.db'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

allheros= [
    {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
    {"name": "Doreen Green", "super_name": "Squirrel Girl"},
    {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
    {"name": "Janet Van Dyne", "super_name": "The Wasp"},
    {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
    {"name": "Carol Danvers", "super_name": "Captain Marvel"},
    {"name": "Jean Grey", "super_name": "Dark Phoenix"},
    {"name": "Ororo Munroe", "super_name": "Storm"},
    {"name": "Kitty Pryde", "super_name": "Shadowcat"},
    {"name": "Elektra Natchios", "super_name": "Elektra"},
]

@app.route('/')
def home():
    return ''
@app.route('/heroes')
def heroes():
    return jsonify(allheros)



@app.route('/add-dumy')
def add_dumy():
    hero =Hero(name='Mojo Jojo',super_name='Crazy Ape')
    db.session.add(hero)
    db.session.commit()
    return "Hero added"

if __name__ == '__main__':
    app.run(port=5555,debug=True)
