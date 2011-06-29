#!/usr/bin/env python
# encoding: utf-8

import peewee
from base import BaseModel


class User(BaseModel):
    username = peewee.CharField()
    password = peewee.CharField()
