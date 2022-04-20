from app import db
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_dance.consumer.storage.sqla import (OAuthConsumerMixin,
                                               SQLAlchemyStorage)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), unique=True)
    name = db.Column(db.String(256))
    is_artist = db.Column(db.String(256)) # If the user is registered as an artist, is_artist == 1


class OAuth(OAuthConsumerMixin, db.Model):
    provider_user_id = db.Column(db.String(256), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(256))
    spotify_player = db.Column(db.String(256))
    artist_genre_primary = db.Column(db.String(256))
    artist_genre_secondary = db.Column(db.String(256))
    user_email = db.Column(db.String(256)) # this is to match artist with its user


db.create_all()