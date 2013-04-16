# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
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

def listar(write_tmpl,tmpl,estado_id):
    estado_id=long(estado_id)
    estado=Estado.get_by_id(estado_id)
    values={"estado":estado,

            "list_url":router.to_path(listar_ajax,estado_id)}
    write_tmpl("/geo/templates/cidade_list.html",values)

def listar_ajax(resp,estado_id,offset="0"):
    PAGE_SIZE=2
    estado_id=long(estado_id)
    estado_key=ndb.Key(Estado,estado_id)
    query=Cidade.query(Cidade.estado==estado_key).order(Cidade.nome)
    offset=long(offset)
    cidades=query.fetch(PAGE_SIZE,offset=offset)
    cidades=[{"id":c.key.id(),"nome":c.nome} for c in cidades]
    offset+=PAGE_SIZE
    next_page_url=router.to_path(listar_ajax,estado_id,offset)
    dct={"nextPageUrl":next_page_url,
         "cidades":cidades}
    js=json.dumps(dct)
    resp.write(js)
