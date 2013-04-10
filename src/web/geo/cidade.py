# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from core.geo.model import Estado, Cidade
from zen import router


def form(write_tmpl):
    estados=Estado.query().order(Estado.nome)
    values={"estados":estados,
            "save_url": router.to_path(salvar)}
    write_tmpl("/geo/templates/cidade_form.html",values)


def salvar(handler,nome,estado_id):
    estado_id=long(estado_id)
    estado_key=ndb.Key(Estado,estado_id)
    cidade=Cidade(nome=nome,estado=estado_key)
    cidade.put()
    handler.redirect(router.to_path(listar,estado_id))

def listar(write_tmpl,estado_id,offset="0"):
    PAGE_SIZE=2;
    estado_id=long(estado_id)
    estado=Estado.get_by_id(estado_id)
    query=Cidade.query(Cidade.estado==estado.key).order(Cidade.nome)
    offset=long(offset)
    cidades=query.fetch(PAGE_SIZE,offset=offset)
    offset+=PAGE_SIZE
    next_page_url=router.to_path(listar,estado_id,offset)
    values={"estado":estado,
            "cidades":cidades,
            "next_page_url":next_page_url}
    write_tmpl("/geo/templates/cidade_list.html",values)
