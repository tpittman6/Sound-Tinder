from app import db
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_dance.consumer.storage.sqla import (OAuthConsumerMixin,
                                               SQLAlchemyStorage)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), unique=True)
    name = db.Column(db.String(256))

class OAuth(OAuthConsumerMixin, db.Model):
    provider_user_id = db.Column(db.String(256), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)


db.create_all()
