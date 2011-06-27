#!/usr/bin/env python
# encoding: utf-8

"""
Sniptr's main module.

Here's defined the URL mapping for the app
and all the behaviour.
"""

from flask import g, Module, render_template
from lib.model.snipet import Snipet

sniptr = Module(__name__)


@sniptr.route("/")
def index():
    snipets = [x for x in Snipet.select().order_by(("date", "desc"))]
    print snipets
    return render_template("index.html", snipets=snipets)
