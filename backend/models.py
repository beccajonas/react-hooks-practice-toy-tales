from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
import string, datetime

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)
db = SQLAlchemy(metadata=metadata)

class Toys(db.Model, SerializerMixin):
    __tablename__ = "toy_table"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    likes = db.Column(db.Integer)
    user= db.Column(db.String)

class Users(db.Model, SerializerMixin):
    __tablename__ = "user_table"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    toys = db.Column(db.String)


