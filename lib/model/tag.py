#!/usr/bin/env python
# encoding: utf-8

import peewee
from base import BaseModel


class Tag(BaseModel):
    name = peewee.CharField()
