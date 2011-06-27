#!/usr/bin/env python
# encoding: utf-8

"""
Sniptr's main module.

Here's defined the URL mapping for the app
and all the behaviour.
"""

from flask import Module, g


sniptr = Module(__name__)


@sniptr.route("/")
def index():
    return "HI!"
