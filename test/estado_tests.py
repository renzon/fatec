# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest
from google.appengine.ext import testbed
from core.geo.model import Estado
from core.web import tmpl
from web.geo import estado
from zen import router


class HandlerMock(object):
    def redirect(self, url):
        self.url = url


class EstadoTests(unittest.TestCase):
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def test_salvar(self):
        handler = HandlerMock()
        estado.salvar(handler, "Sao Paulo", "SP", "11")
        salvo = Estado.query().get()
        self.assertEqual("Sao Paulo", salvo.nome)
        self.assertEqual("SP", salvo.sigla)
        self.assertEqual(11, salvo.ddd)
        url = router.to_path(estado.listar)
        self.assertEqual(url, handler.url)

    def test_listar(self):
        def write_tmpl(tmpl_name, dct):
            self.tmpl_name = tmpl_name
            self.values = dct
            tmpl.render(tmpl_name, dct)

        estado.listar(write_tmpl)
        self.assertEqual("/geo/templates/state_list.html", self.tmpl_name)
        self.assertDictEqual({"estados": [],
                              "apagar_url": router.to_path(estado.apagar),
                              "editar_url": router.to_path(estado.editar)},
                             self.values)

    def test_editar(self):
        def write_tmpl(tmpl_name, dct):
            tmpl.render(tmpl_name, dct)

        salvo=Estado(nome="1",sigla="2",ddd=1)
        salvo.put()
        handler = HandlerMock()
        id=salvo.key.id()
        estado.salvar(handler, "Sao Paulo", "SP", "11",str(id))
        editado=salvo.key.get()
        self.assertEqual("Sao Paulo", editado.nome)
        self.assertEqual("SP", editado.sigla)
        self.assertEqual(11, editado.ddd)


