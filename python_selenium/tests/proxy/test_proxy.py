"""
./python_selenium/tests/proxy/test_proxy.py
+++++++++++++++++++++++++++++++++++++++++++

Tests for proxy.py

| Author: shmakovpn <shmakovpn@yandex.ru>
| Date: 2021-01-28
"""
from unittest import TestCase
from unittest import mock
from unittest.mock import PropertyMock, patch
from python_selenium.proxy import Proxy


class TestProxy(TestCase):
    """Testing the Proxy class"""
    def test_defaults(self) -> None:
        """Testing default values"""
        proxy: Proxy = Proxy()
        self.assertEqual(proxy.protocol, 'http')
        self.assertEqual(proxy.ip, '')
        self.assertEqual(proxy.port, 80)
        self.assertEqual(proxy.login, '')
        self.assertEqual(proxy.password, '')

    def test__auth(self) -> None:
        """Testing getter of an authentication part of the proxy URL"""
        proxy: Proxy = Proxy()
        proxy.login = ''
        proxy.password = ''
        self.assertEqual(proxy._auth, '')  # type: ignore
        proxy.login = 'python'
        self.assertEqual(proxy._auth, 'python@')  # type: ignore
        proxy.password = 'the_best'
        self.assertEqual(proxy._auth, 'python:the_best@')  # type: ignore

    @patch.object(Proxy,
                  '_auth',
                  new_callable=PropertyMock)
    def test_url(self, mock__auth: PropertyMock) -> None:
        """Testign getter of the proxy URL"""
        mock__auth.side_effect = lambda: 'L:P@'
        proxy: Proxy = Proxy()
        proxy.ip = ''
        proxy.port = 81
        proxy.protocol = 'HTTP'
        self.assertEqual(proxy.url, '')
        mock__auth.assert_not_called()
        proxy.ip = 'IP'
        self.assertEqual(proxy.url, 'HTTP://L:P@IP:81')
        mock__auth.assert_called_once_with()

    @patch.object(Proxy, 'url', new_callable=PropertyMock)
    def test__str(self, mock_url: PropertyMock) -> None:
        """Testing __str__ of Proxy"""
        mock_url.side_effect = lambda: 'URL'
        proxy: Proxy = Proxy()
        self.assertEqual(str(proxy), 'URL')
        mock_url.assert_called_once_with()
