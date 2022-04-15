from app import app, db
import random
import os
import flask
from flask import Flask

# this was a test function for google login -- still might need it, not sure
def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401) # Authorization required
        else:
            return function()
    return wrapper


@app.route("/login")
def login():
    return flask.redirect("/welcome_user")


# This is part of the google login tutorial -- not sure if it will stay
@app.route("/callback")
def callback():
    pass


# We may not need this if we can sign up or login on the same page with google oauth
@app.route("/signup")
def signup():
    pass


@app.route("/logout")
def logout():
    return flask.redirect(
        "/"
    )


# This will be the 'landing page' -- decorate index.html with all landing page stuff
# This will be where you login as well
@app.route("/")
def index():
    return flask.render_template(
        "index.html",
    )


# This is where you will be redirected after successfully logging in
@app.route("/welcome_user")
def welcome_user():
    return flask.render_template(
        "welcome_user.html",
    )


# Profile info page
@app.route("/profile")
def profile():
    return flask.render_template(
        "profile.html",
    )

# This is the page that the 'swiping' will be done on
@app.route("/discover")
def discover():
    return flask.render_template(
        "discover.html",
    )

if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 5000)),
        debug=True,
    )
