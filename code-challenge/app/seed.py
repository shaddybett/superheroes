from app import app,db
from models import Hero

def seed_heros():
    with app.context():
        