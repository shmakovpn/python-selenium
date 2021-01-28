"""
./python_selenium/tests/proxy/test_proxy.py
+++++++++++++++++++++++++++++++++++++++++++

Test for proxy.py

| Author: shmakovpn <shmakovpn@yandex.ru>
| Date: 2021-01-28
"""
from unittest import TestCase
from python_selenium.proxy import Proxy


class TestProxy(TestCase):
    def setUp(self) -> None:
        self.proxy: Proxy = Proxy()
        return super().setUp()

    def test_defaults(self) -> None:
        self.assertEqual(self.proxy.protocol, 'http')
        self.assertEqual(self.proxy.ip, '')
        self.assertEqual(self.proxy.port, 80)
        self.assertEqual(self.proxy.login, '')
        self.assertEqual(self.proxy.password, '')