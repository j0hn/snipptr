#!/usr/bin/env python
# encoding: utf-8

"""
Snippet. A short peace of handfull code.
"""

import peewee
from base import BaseModel
from tag import Tag


class Snippet(BaseModel):
    title = peewee.CharField()
    text = peewee.CharField()
    date = peewee.CharField()
    language = peewee.CharField()

    def get_tags(self):
        return [x.tag for x in SnippetTag.select().where(snippet=self)]

class SnippetTag(BaseModel):
    snippet = peewee.ForeignKeyField(Snippet)
    tag = peewee.ForeignKeyField(Tag)
