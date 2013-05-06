# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


def seguranca(fcn_de_negocio):

    def fcn(valor,*args,**kwargs):
        print args
        if valor>0:
            fcn_de_negocio(valor,*args,**kwargs)
        else:
            print "funcao nao permitida"
    return fcn

@seguranca
def sacar(valor,*args):
    print "Dentro do sacar"
    print args
    print "sacando %s"% valor

@seguranca
def debitar(valor,saldo=6):
    print saldo
    print "sacando %s"% valor

sacar(20,"Renzo","Nuccitelli")
debitar(2,saldo=8)

