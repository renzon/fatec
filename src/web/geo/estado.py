# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from core.geo.model import Estado
from core.usuario import seg
from zen import router

@seg.usuario_logado
def form(write_tmpl):
    values={"save_url":router.to_path(salvar)}
    write_tmpl("/geo/templates/form.html",values)


def salvar(handler,nome, sigla, ddd,id=None):
    ddd=long(ddd)
    if id:
        estado=Estado(id=long(id),nome=nome,sigla=sigla,ddd=ddd)
    else:
        estado=Estado(nome=nome,sigla=sigla,ddd=ddd)
    estado.put()
    handler.redirect(router.to_path(listar))

def listar(write_tmpl):
    query=Estado.query(Estado.ddd>0).order(Estado.ddd)
    # query=query.filter(Estado.ddd>0)
    # query=query.order(Estado.ddd)
    estados=query.fetch(100)
    values={"estados":estados,
            "apagar_url":router.to_path(apagar),
            "editar_url":router.to_path(editar)}
    write_tmpl("/geo/templates/state_list.html",values)

def apagar(handler,id):
    key=ndb.Key(Estado,long(id))
    key.delete()

def editar(write_tmpl,urlsafe):
    key=ndb.Key(urlsafe=urlsafe)
    estado=key.get()
    values={"save_url":router.to_path(salvar),
            "estado":estado}
    write_tmpl("/geo/templates/form.html",values)
