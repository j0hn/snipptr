#!/usr/bin/env python
# encoding: utf-8

"""
Snipptr's main module.

Here's defined the URL mapping for the app
and all the behaviour.
"""

from flask import g, Module, render_template
from lib.model.snippet import Snippet

snipptr = Module(__name__)


@snipptr.route("/")
def index():
    snippets = [x for x in Snippet.select().order_by(("date", "desc"))]
    print snippets
    return render_template("index.html", snippets=snippets)
