# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import unittest
from google.appengine.ext import testbed
from core.geo.model import Estado
from web.geo import estado


class GAETestCase(unittest.TestCase):
    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.setup_env(app_id="_")
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_user_stub()
        self.testbed.init_urlfetch_stub()
        self.testbed.init_memcache_stub()
        self.testbed.init_mail_stub()
        self.testbed.init_taskqueue_stub()

    def tearDown(self):
        self.testbed.deactivate()

class HandlerStub(object):
    def __init__(self):
        self.redirect_url=None

    def redirect(self,url):
        self.redirect_url=url

class EstadoTests(GAETestCase):
    def test_salvar(self):
        handler=HandlerStub()
        estado.salvar(handler, "SPE", "SP", "11")
        salvo=Estado.query().get()
        self.assertEqual("SPE",salvo.nome)
        self.assertEqual("SP",salvo.sigla)
        self.assertEqual(11,salvo.ddd)