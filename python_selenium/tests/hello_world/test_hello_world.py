"""
python_selenium/tests/hello_world/test_hello_world.py
+++++++++++++++++++++++++++++++++++++++++++++++++++++

This script just checks that tests work

| Author: shmakovpn <shmakovpn@yandex.ru>
| Date: 2021-01-14
"""
from unittest import TestCase


class TestHelloWorld(TestCase):
    """Checks that the testing works itself"""
    def test_hello_world(self):
        self.assertEqual('Hello world', "Hello world")
