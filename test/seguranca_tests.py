# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from cola import GAETestCase
from core.usuario import seg
from core.usuario.model import Usuario


@seg.usuario_logado
def handle_stub():
    return "stub executado"

class HandlerStub():
    def redirect(self,url):
        self.url=url

GOOGLE_ID="12"
class GoogleUserMock():
    def user_id(self):
        return GOOGLE_ID

class SegurancaTests(GAETestCase):
    def test_usuario_logado_decorator(self):
        #usuario nao logado no google
        seg.users.get_current_user= lambda : None
        handler=HandlerStub()
        handle_stub({},handler)
        #to do

        #logado no google
        seg.users.get_current_user= lambda : GoogleUserMock()
        handle_stub({},handler)
        self.assertEqual("/usuario/form",handler.url)

        #usuario ja cadastrado
        Usuario(nome="Renzo",email="blah",google_id=GOOGLE_ID).put()
        retorno=handle_stub({},handler)
        self.assertEqual("stub executado",retorno)


