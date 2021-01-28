"""
python_selenium/proxy.py
++++++++++++++++++++++++

| Author: shmakovpn "shmakovpn<yandex.ru>"
| Date: 2012-01-28
"""


class Proxy:
    """
    Proxy configuration
    """
    protocol: str = 'http'
    """The protocol of the proxy: *'http'*, *'https'* or *'socks'*.
    Default to *'http'*."""

    ip: str = ''
    """The IP address of the proxy.
    Default to the empty string (proxy isn't using)."""

    port: int = 80
    """The TCP port of the proxy.
    Default to 80."""

    login: str = ''
    """The username of the proxy user.
    Default to the empty string (authentication isn't using)."""

    password: str = ''
    """The password of the proxy user.
    Default to the empty string."""
    @property
    def _auth(self) -> str:
        """
        Returns an authentication part of the proxy URL
        """
        if not self.login:
            return ''
        if not self.password:
            return f'{self.login}@'
        return f'{self.login}:{self.password}@'

    @property
    def url(self) -> str:
        """
        Returns the proxy URL
        """
        if not self.ip:
            return ''
        return f'{self.protocol}://{self._auth}{self.ip}:{self.port}'

    def __str__(self) -> str:
        return self.url