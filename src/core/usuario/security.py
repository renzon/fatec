# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from core.web import decorator_util


# def allow_logged(fcn):
#     def wrapper(_dependencies,*args,**kwargs):
#         deps=decorator_util.find_dependencies(_dependencies,fcn)
#         deps.extend(args)
#         return fcn(*deps,**kwargs)
#     return wrapper
