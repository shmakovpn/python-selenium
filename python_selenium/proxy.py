"""
python_selenium/proxy.py
++++++++++++++++++++++++

| Author: shmakovpn "shmakovpn<yandex.ru>"
| Date: 2012-01-28
"""


class Proxy:
    """
    Proxy configuration
    
    :param str protocol: The protocol of the proxy: *'http'*, *'https'* or *'socks'*.\
        Defaults to *'http'*.
    :param str ip: The IP address of the proxy.\
        Default to the empty string (proxy isn't using).
    :param int port: The TCP port of the proxy.\
        Default to 80.
    :param str login: The username of the proxy user.\
        Default to the empty string (authentication isn't using).
    :param str password: The password of the proxy user.\
        Default to the empty string.
    """
    def __init__(self,
                 protocol: str = 'http',
                 ip: str = '',
                 port: int = 80,
                 login: str = '',
                 password: str = '') -> None:
        self.protocol = protocol
        self.ip = ip
        self.port = port
        self.login = login
        self.password = password

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

    # @property
    # def to_dict(self) -> Dict[str, str]:
    #     return {
    #         'http': f'{self.ip}:{self.port}',
    #         'https': f'{self.ip}:{self.port}',
    #         'socks': f'{self.ip}:{self.port}',
    #     }

    def __str__(self) -> str:
        return self.url