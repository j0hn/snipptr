#!/usr/bin/env python
# encoding: utf-8

"""
BaseModel.

Defines the basic database model and
the ORM connection.
"""

import peewee


database = peewee.Database(peewee.SqliteAdapter(), "sniptr.db")

class BaseModel(peewee.Model):
    """
    Base table model.
    """

    class Meta:
        database = database
