# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import inspect


def find_dependencies(_dependencies,fcn):
    args=inspect.getargspec(fcn)[0]
    return [_dependencies[a] for a in args if a in _dependencies]


if __name__=="__main__":
    dep={"a":"av","b":"bv"}
    def f(a,b): pass
    print find_dependencies(dep,f)
