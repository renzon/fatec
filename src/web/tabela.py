# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class Professor(object):
    def __init__(self,nome="Renzo",idade=30,salario=100):
        self.nome=nome
        self.idade=idade
        self.salario=salario

def index(write_tmpl):
    alunos=["Shen","Lessa","Mengussi","Fabio"]
    professores=[Professor(),Professor("Massanori",35,200)]
    values={"alunos":alunos,"professores":professores}
    write_tmpl("/templates/table.html",values)


