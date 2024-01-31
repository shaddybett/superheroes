
from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower
import os
from wtforms import Form, StringField, validators

abs_path = os.getcwd()
db_path = f"{abs_path}/db/app.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route("/")
def home():
    return "This is the home page. Please use the /api/heroes endpoint to get and post heroes."


@app.route("/heroes", methods=["GET"])
def get_heroes():
    heroes = Hero.query.all()
    heroes_data = [
        {"id": hero.id, "name": hero.name, "super_name": hero.super_name}
        for hero in heroes
    ]
    return jsonify(heroes_data)


@app.route("/heroes/<int:hero_id>", methods=["GET"])
def get_hero_by_id(hero_id):
    hero = Hero.query.get(hero_id)

    if hero:
        hero_data = {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
            "powers": [
                {"id": power.id, "name": power.name, "description": power.description}
                for power in hero.powers
            ]
            if hasattr(hero, "powers")
            else [],
        }
        return jsonify(hero_data)
    else:
        return make_response(jsonify({"error": "Hero not found"}), 404)


@app.route("/powers", methods=["GET"])
def get_powers():
    powers = Power.query.all()
    powers_data = [
        {"id": power.id, "name": power.name, "description": power.description}
        for power in powers
    ]
    return jsonify(powers_data)


@app.route("/powers/<int:power_id>", methods=["GET", "PATCH"])
def get_or_update_power(power_id):
    power = Power.query.get(power_id)

    if not power:
        return make_response(jsonify({"error": "Power not found"}), 404)

    if request.method == "GET":
        power_data = {
            "id": power.id,
            "name": power.name,
            "description": power.description,
        }
        return jsonify(power_data)
    elif request.method == "PATCH":
        data = request.get_json()

        if "description" in data:
            power.description = data["description"]
            db.session.commit()
            updated_power_data = {
                "id": power.id,
                "name": power.name,
                "description": power.description,
            }
            return jsonify(updated_power_data)
        else:
            return make_response(
                jsonify({"errors": ["Missing 'description' in request"]}), 400
            )


class HeroPowerForm(Form):
    strength = StringField('Strength', [validators.DataRequired()])
@app.route("/hero_powers", methods=["POST"])
def create_hero_power():
        form = HeroPowerForm(request.form)

        if form.validate():
            

            data = request.get_json()

            if not all(key in data for key in ["strength", "power_id", "hero_id"]):
                return make_response(
                    jsonify({"errors": ["Missing required fields in request"]}), 400
                )

            hero = Hero.query.get(data["hero_id"])

            if not hero:
                return make_response(jsonify({"error": "Hero not found"}), 404)

            new_hero_power = HeroPower(
                strength=data["strength"], power_id=data["power_id"], hero_id=data["hero_id"]
            )

            db.session.add(new_hero_power)
            db.session.commit()

            # Instead of directly returning the result of get_hero_by_id, construct a JSON-friendly response
            hero_data = {
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name,
                "powers": [
                    {"id": power.id, "name": power.name, "description": power.description}
                    for power in hero.powers
                ]
                if hasattr(hero, "powers")
                else [],
            }
    
            return jsonify(hero_data)
        else:
            return make_response(
                jsonify({"errors": form.errors}), 400
            )

if __name__ == "__main__":
    app.run(port=3001, debug=True)
