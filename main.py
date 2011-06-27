#!/usr/bin/env python
# encoding: utf-8

"""
Sniptr. Simple snipet save webpage.

Saves snipets of any programming language you want.
You can tag them, and visualize them with color highlighting.
"""

from os import urandom
from flask import g, Flask

from lib.sniptr import sniptr
from lib.model.base import database

DEBUG = True
SECRET_KEY = urandom(25)

# We create the app and register the sniptr module
app = Flask(__name__)
app.register_module(sniptr)


@app.before_request
def before_request():
    """
    Ran before any HTTP request.
    Connects the database.
    """

    g.db = database
    g.db.connect()


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
