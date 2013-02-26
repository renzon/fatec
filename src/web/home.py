# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from web import ola
from zen import router


def index(handler):
    url=router.to_path(ola.index,"Andre","Menegussi")
    handler.redirect(url)