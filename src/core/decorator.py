# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


def seguranca(fcn_de_negocio):
    def fcn(valor):
        if valor>0:
            fcn_de_negocio(valor)
        else:
            print "funcao nao permitida"
    return fcn

@seguranca
def sacar(valor):
    print "sacando %s"% valor

@seguranca
def debitar(valor):
    print "sacando %s"% valor








sacar(-20)
debitar(-2)

