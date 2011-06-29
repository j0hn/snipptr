#!/usr/bin/env python
# encoding: utf-8

"""
Snipptr. Simple snippet save webpage.

Saves snippets of any programming language you want.
You can tag them, and visualize them with color highlighting.
"""

from os import urandom
from flask import g, Flask, session, render_template

from lib.snipptr import snipptr
from lib.model.base import database
from lib.model.user import User

DEBUG = True
SECRET_KEY = urandom(25)

# We create the app and register the snipptr module
app = Flask(__name__)
app.register_module(snipptr)


@app.errorhandler(404)
def page_not_found(e):
        return render_template('404.html')


@app.before_request
def before_request():
    """
    Ran before any HTTP request.
    Connects the database.
    """

    g.db = database
    g.db.connect()

    try:
        g.user = [x for x in User.select().where(id=session["user_id"])].pop()
    except:
        g.user = None


@app.after_request
def after_request(response):
    """
    Ran after any HTTP request.
    Disconnects the database.
    """

    g.db.close()
    return response


if __name__ == "__main__":
    app.config.from_object(__name__)
    app.run("0.0.0.0")
