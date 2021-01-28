"""
ping.eu.py
++++++++++

Opens ping.eu over proxy

| Author: shmakovpn <shmakovpn@yandex.ru>
| Date: 2021-01-27
"""
from typing import List
# from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

DEBUG: bool = True


def ping_eu_ip(proxy: Proxy) -> str:
    proxy_options = {proxy: {'https': '{proxy[0]}://{login}:{password}@'}}
    chrome_options: Options = webdriver.ChromeOptions()
    useragent: UserAgent = UserAgent()
    chrome_options.add_argument(f'user-agent={useragent.random}')
    if not DEBUG:
        chrome_options.add_experimental_option(
            "prefs", {"profile.managed_default_content_settings.images": 2})
        chrome_options.add_argument("--silent")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--log-level=3')
    if proxy:
        # chrome_options.add_argument(f'--proxy-server=//{proxy[1]}:{proxy[2]}')
        chrome_options.add_argument(
            f'--proxy-server={proxy[0]}://{proxy[1]}:{proxy[2]}')
    # driver: webdriver.Chrome = webdriver.Chrome(options=chrome_options)
    driver: webdriver.Chrome = webdriver.Chrome(
        seleniumwire_options=proxy_options)
    try:
        # driver.get('http://ping.eu/')
        driver.get('https://2ip.ru/')
        waiter: WebDriverWait = WebDriverWait(driver, 8)
        try:
            ip_element: WebElement = waiter.until(
                EC.visibility_of_element_located(
                    (By.XPATH, '//td[@class="txt14"]/b')))
            ip: str = ip_element.text
            return ip
        except Exception as e:
            print(f'waiting failed: {e}')
    except WebDriverException as e:
        print(f'A WebDriverException has occurred: {e}')
    finally:
        try:
            driver.close()
        except Exception as e:
            print(f'An exception has occurred while drive.close(): {e}')
    return ''


def main() -> None:
    proxies: List[Proxy] = [
        ('http', '67.207.83.225', 80),
    ]
    for proxy in proxies:
        print(ping_eu_ip(proxy))
    print('main finished')


if __name__ == '__main__':
    main()