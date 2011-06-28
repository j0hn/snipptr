#!/usr/bin/env python
# encoding: utf-8

"""
Creates the database tables.
"""

import peewee

from snippet import Snippet
from base import database


def create_tables():
    """
    Creates the tables.
    """

    database.connect()
    Snippet.create_table()


def fill_with_content():
    """
    Fills with sample content.
    """

    Snippet.get_or_create(title="Create os dir in python",
                         text="import os\n"\
                              "os.mkdir('FOLDER_NAME')")
    Snippet.get_or_create(title="Get command line arguments in C",
                         text="""int main(int *argc, char *argv[]){}""")


if __name__ == "__main__":
    try:
        create_tables()
        print "Tables created"
    except:
        print "Tables Allready created"

    fill_with_content()
    print "Tables filled with content"
