# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


def world(resp):
    resp.write("Hello World")

def index(resp,name="",surname=""):
    resp.write("Home %s %s"%(name,surname))

