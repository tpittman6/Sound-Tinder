from app import app, db
import os
from models import User, OAuth
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import (LoginManager, UserMixin,
                         current_user, login_user, logout_user)
from flask_dance.consumer import oauth_authorized
from flask_dance.contrib.google import make_google_blueprint, google
from dotenv import find_dotenv, load_dotenv
from flask_dance.consumer.storage.sqla import (OAuthConsumerMixin,
                                               SQLAlchemyStorage)

load_dotenv(find_dotenv())

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'google.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

google_blueprint = make_google_blueprint(
    client_id=os.getenv('GOOGLE_CLIENT_ID'),
    client_secret=os.getenv('GOOGLE_CLIENT_SECRET'),
    scope="openid https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile",
    offline=True,
    reprompt_consent=True,
    storage=SQLAlchemyStorage(OAuth, db.session, user=current_user)
)

app.register_blueprint(google_blueprint)

# This will be the 'landing page' -- decorate index.html with all landing page stuff
# This will be where you login as well
@app.route('/')
def index():
    google_data = None
    user_info_endpoint = '/oauth2/v2/userinfo'
    if current_user.is_authenticated and google.authorized:
        google_data = google.get(user_info_endpoint).json()
    return render_template('home.html',
                           google_data=google_data,
                           fetch_url=google.base_url + user_info_endpoint)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@oauth_authorized.connect_via(google_blueprint)
def google_logged_in(blueprint, token):
    resp = blueprint.session.get('/oauth2/v2/userinfo')
    user_info = resp.json()
    user_id = str(user_info['id'])
    oauth = OAuth.query.filter_by(provider=blueprint.name,
                                  provider_user_id=user_id).first()
    if not oauth:
        oauth = OAuth(provider=blueprint.name,
                      provider_user_id=user_id,
                      token=token)
    else:
        oauth.token = token
        db.session.add(oauth)
        db.session.commit()
        login_user(oauth.user)
    if not oauth.user:
        user = User(email=user_info["email"],
                    name=user_info["name"])
        oauth.user = user
        db.session.add_all([user, oauth])
        db.session.commit()
        login_user(user)

    return False


# This is where you will be redirected after successfully logging in
@app.route("/home")
def home():
    user = dict(session)['profile']['email']
    return render_template(
        "home.html",
        user=user,
    )


# Profile info page
@app.route("/profile")
def profile():
    return render_template(
        "profile.html",
    )

# This is the page that the 'swiping' will be done on
@app.route("/discover")
def discover():
    return render_template(
        "discover.html",
    )

if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 5000)),
        debug=True,
    )
