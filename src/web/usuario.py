# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.api import users
from core.usuario.model import Usuario
from zen import router


def form(write_tmpl,handler):
    google_user=users.get_current_user()
    usuario=Usuario.current_user()
    if usuario:
        handler.redirect("/")
    else:
        values={"url_salvar":router.to_path(salvar),
                "email":google_user.email()}
        write_tmpl("/templates/cadastro_usuario.html",values)


def salvar(handler, nome, email):
    google_user=users.get_current_user()
    Usuario(nome=nome,email=email,google_id=google_user.user_id()).put()
    handler.redirect("/")
