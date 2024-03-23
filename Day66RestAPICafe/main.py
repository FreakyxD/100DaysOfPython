from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        dictionary = {}

        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")  # methods=["GET"] can be omitted
def get_random_cafe():
    row_count = db.session.query(Cafe).count()
    if row_count == 0:
        return jsonify(error={"Not Found": "Sorry, we don't know any cafes."}), 404
    choice_id = random.randint(1, row_count)
    cafe = db.get_or_404(Cafe, choice_id)
    return jsonify(cafe=cafe.to_dict())


@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = result.scalars().all()

    if not all_cafes:
        return jsonify(error={"Not Found": "Sorry, we don't know any cafes."}), 404
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/search")
def search():
    search_term = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == search_term))
    all_cafes = result.scalars().all()

    if not all_cafes:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=request.form.get("has_toilet", "").lower() == "true",  # comparison results in a boolean; "" if no
        # data in form field
        has_wifi=request.form.get("has_wifi", "").lower() == "true",
        has_sockets=request.form.get("has_sockets", "").lower() == "true",
        can_take_calls=request.form.get("can_take_calls", "").lower() == "true",
        coffee_price=request.form.get("coffee_price")
    )

    db.session.add(new_cafe)
    db.session.commit()

    return jsonify({"success": "Cafe added successfully."}), 201


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def change_price(cafe_id):
    cafe_to_update = db.session.get(Cafe, cafe_id)
    if cafe_to_update:
        cafe_to_update.coffee_price = request.args.get("new_price")
        db.session.commit()
        return jsonify(response={"success": "Coffee price updated successfully."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    api_key = "TopSecretAPIKey"
    user_api_key = request.args.get("api-key")
    if not user_api_key:
        return jsonify(error={"Not Authorized": "Please provide an api key."}), 403

    if user_api_key == api_key:
        cafe_to_delete = db.session.get(Cafe, cafe_id)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": "Cafe deleted successfully."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404

    else:
        return jsonify(error={"Not Authorized": "Wrong api key."}), 403


if __name__ == '__main__':
    app.run(debug=True)
