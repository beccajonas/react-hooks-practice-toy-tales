from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import datetime
from models import db, Toys
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.get('/')
def index():
    return "toy backend"

@app.get('/toys/')
def get_toys():
    #python object
    toys = Toys.query.all()
    #convert each nested python object into json
    return [toy.to_dict() for toy in toys]

@app.get('/toys/<int:id>')
def get_toys_by_id(id):
    toy = Toys.query.filter_by(id=id).first()
    return toy.to_dict()


@app.patch('/toys/<int:id>')
def patch_toys(id):
    toy = db.session.get(Toys, id)
    data = request.json
    for key in data:
        setattr(toy, key, data[key])
        # setattr(object, name, value)
    db.session.add(toy)
    db.session.commit()
    # return the new toy with updated attributes
    return toy.to_dict()

@app.delete('/toys/<int:id>')
def delete_toys(id):
    toy = db.session.get(Toys, id)
    db.session.delete(toy)
    db.session.commit()
    return {}

@app.post('/toys')
def post_toys():
    data = request.json
    new_toy = Toys(name=data['name'], image=data['image'], likes=0)
    db.session.add(new_toy)
    db.session.commit()
    return new_toy.to_dict()

if __name__ == "__main__":
    app.run(port=5555, debug=True)