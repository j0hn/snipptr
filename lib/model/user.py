#!/usr/bin/env python
# encoding: utf-8

import peewee
from base import BaseModel


class User(BaseModel):
    username = peewee.CharField()
    password = peewee.CharField()

    def get_anon(self):
        anon = self.get_or_create(username="Anonymous", password="jgiueqjnas")
        return anon
