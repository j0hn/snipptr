#!/usr/bin/env python
# encoding: utf-8

"""
Snipptr's main module.

Here's defined the URL mapping for the app
and all the behaviour.
"""

import time
from itertools import chain
from flask import g, Module, render_template, request, redirect, url_for, \
        abort, session

from lib.model.snippet import Snippet, SnippetTag
from lib.model.tag import Tag
from lib.model.user import User

snipptr = Module(__name__)


def flatten(listOfLists):
    return chain.from_iterable(listOfLists)


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
    tags = [x.split() for x in request.form.get("tags").split(",")]
    tags = [x.strip() for x in flatten(tags)]

    if not g.user:
       user = User().get_anon()
    else:
       user = g.user

    snip = Snippet.create(title=title, text=text,
                          date=str(time.time()), user=user)

    for tag_name in tags:
        tag = Tag.get_or_create(name=tag_name.lower())
        SnippetTag.get_or_create(snippet=snip, tag=tag)

    return redirect(url_for("index"))


@snipptr.route("/view_tag/<tag_name>")
def view_tag(tag_name):
    try:
        tag = Tag.get(name=tag_name.lower())
    except:
        abort(404)

    snippets = [x.snippet for x in SnippetTag.select().where(tag=tag)]

    return render_template("view_tag.html", tag=tag, snippets=snippets)


@snipptr.route("/login", methods=["POST", "GET"])
def login():
    if g.user:  # Allready logged in
        return redirect(url_for("index"))

    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        try:
            user = [x for x in User.select().where(username=username, password=password)].pop()
            session["user_id"] = user.id
            return redirect(url_for("index"))
        except Exception, e:
            print e
            error = "Invalid username or password"

    return render_template("login.html", error=error)



@snipptr.route("/logout")
def logout():
    session.pop('user_id', None)
    return redirect(url_for("index"))
