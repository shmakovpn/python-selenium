"""
python_selenium/aiohttp.2ip.ru
++++++++++++++++++++++++++++++

aiohttp request example

| Author: shmakovpn <shmakovpn@yandex.ru>
| Date: 2021-01-28
"""
from typing import List
import asyncio
from asyncio.futures import Future
from asyncio import AbstractEventLoop
from aiohttp.client import ClientSession
#
import aiohttp
from aiohttp.client_exceptions import ClientProxyConnectionError
#
from bs4 import BeautifulSoup
#
from python_selenium.proxy import Proxy

# 206.189.189.81	3128	US	United States	anonymous	no	yes	1 minute ago
# 51.75.147.41	3128

proxies: List[Proxy] = [
    # Proxy(ip='206.189.189.81', port=3128, protocol='http'),
    # Proxy(ip='51.75.147.41', port=3128, protocol='http'),
    # Proxy(ip='193.149.225.181', port=80, protocol='http'),
    # Proxy(ip='176.123.164.240', port=58488, protocol='http'),
    # Proxy(ip='100.24.216.83', port=80, protocol='http'),
    Proxy(ip='100.24.216.83', port=80, protocol='socks'),
]


async def fetch(session: ClientSession, proxy: Proxy) -> None:
    url: str = 'https://2ip.ru/'

    try:
        async with session.get(url, proxy=str(proxy)) as response:
            content = response.content
            print(await content.read())
    except ClientProxyConnectionError as e:
        print(f"Proxy: '{proxy}' doesn't work: {e}")


async def main(proxy: Proxy) -> None:
    print('proxy=', proxy)
    async with aiohttp.ClientSession() as session:
        await fetch(session, proxy)


if __name__ == '__main__':
    print('main begin')
    loop: AbstractEventLoop = asyncio.get_event_loop()
    future: List[Future[None]] = [
        asyncio.ensure_future(main(proxy)) for proxy in proxies
    ]
    loop.run_until_complete(asyncio.wait(future))
    print('main end')
