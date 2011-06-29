#!/usr/bin/env python
# encoding: utf-8

"""
Creates the database tables.
"""

import time
import peewee

from tag import Tag
from user import User
from base import database
from snippet import Snippet, SnippetTag


def create_tables():
    """
    Creates the tables.
    """

    database.connect()
    Snippet.create_table()
    SnippetTag.create_table()
    Tag.create_table()
    User.create_table()


def fill_with_content():
    """
    Fills with sample content.
    """

    j0hn = User.create(username="j0hn", password="negros")

    create_snippet("Create os dir in python",
                   "import os\nos.mkdir('FOLDER_NAME')",
                   ["Python", "os"], j0hn)
    create_snippet("Get command line arguments in C",
                   "int main(int *argc, char *argv[]){}",
                   ["C"])



def create_snippet(title, text, tags_names, user=None):
    if not user:
        user = User().get_anon()

    snip = Snippet.get_or_create(title=title, text=text,
                                 date=str(time.time()), user=user)

    for tag_name in tags_names:
        tag = Tag.get_or_create(name=tag_name.lower())
        SnippetTag.get_or_create(snippet=snip, tag=tag)


if __name__ == "__main__":
    try:
        create_tables()
        print "Tables created"
    except:
        print "Tables Allready created"

    fill_with_content()
    print "Tables filled with content"
