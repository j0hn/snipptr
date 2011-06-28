#!/usr/bin/env python
# encoding: utf-8

"""
Snipptr's main module.

Here's defined the URL mapping for the app
and all the behaviour.
"""

import time
from flask import g, Module, render_template, request, redirect, url_for

from lib.model.snippet import Snippet, SnippetTag
from lib.model.tag import Tag

snipptr = Module(__name__)


@snipptr.route("/")
def index():
    snippets = [x for x in Snippet.select().order_by(("date", "desc"))]
    return render_template("index.html", snippets=snippets)


@snipptr.route("/new_snippet", methods=["POST", "GET"])
def new_snippet():
    if request.method == "GET":
        return render_template("new_snippet.html")

    title = request.form.get("title")
    text = request.form.get("text")
    tags = [x.strip() for x in request.form.get("tags").split(",")]

    # if not g.user:
    #    name = request.form.get("name")
    # else:
    #    name = g.user

    snip = Snippet.create(title=title, text=text, date=str(time.time()))

    for tag_name in tags:
        tag = Tag.get_or_create(name=tag_name)
        SnippetTag.get_or_create(snippet=snip, tag=tag)

    return redirect(url_for("index"))


@snipptr.route("/login")
def login():
    return "hi"


@snipptr.route("/logout")
def logout():
    return "hi"
