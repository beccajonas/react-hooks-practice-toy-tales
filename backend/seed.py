from app import app
from models import Toys, db
import json

if __name__ == '__main__':
    with app.app_context():
        data = {}
        with open ("db.json") as f:
            data = json.load(f)
        Toys.query.delete()

        toy_list = []
        for toy in data["toys"]:
            t = Toys(name=toy.get('name'), image=toy.get('image'), likes=toy.get('likes'))
            toy_list.append(t)

        db.session.add_all(toy_list)
        db.session.commit()