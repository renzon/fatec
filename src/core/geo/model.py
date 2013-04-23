# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb


class Estado(ndb.Model):
    nome=ndb.StringProperty(required=True)
    sigla=ndb.StringProperty(required=True)
    ddd=ndb.IntegerProperty()


class Cidade(ndb.Model):
    nome=ndb.StringProperty(required=True)
    estado=ndb.KeyProperty(Estado,required=True)

