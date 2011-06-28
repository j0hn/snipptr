#!/usr/bin/env python
# encoding: utf-8

"""
Snippet. A short peace of handfull code.
"""

import peewee
from base import BaseModel


class Snippet(BaseModel):
    title = peewee.CharField()
    text = peewee.CharField()
    date = peewee.CharField()
