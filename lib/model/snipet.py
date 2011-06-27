#!/usr/bin/env python
# encoding: utf-8

"""
Snipet. A short peace of handfull code.
"""

import peewee
from base import BaseModel


class Snipet(BaseModel):
    title = peewee.CharField()
    text = peewee.CharField()
    date = peewee.CharField()
