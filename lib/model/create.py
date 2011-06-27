#!/usr/bin/env python
# encoding: utf-8

"""
Creates the database tables.
"""

import peewee

from snipet import Snipet
from base import database


def create_tables():
    """
    Creates the tables.
    """

    database.connect()
    Snipet.create_table()


def fill_with_content():
    """
    Fills with sample content.
    """

    Snipet.get_or_create(title="Create os dir in python",
                         text="import os\n"\
                              "os.mkdir('FOLDER_NAME')")


if __name__ == "__main__":
    try:
        create_tables()
        print "Tables created"
    except:
        print "Tables Allready created"

    fill_with_content()
    print "Tables filled with content"
