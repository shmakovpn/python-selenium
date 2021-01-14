# -*- coding: utf-8 -*-
from typing import Optional, List, TextIO
import argparse
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.chrome.options import Options
import sys
from io import StringIO
from unittest.mock import patch

DEBUG: bool = False
VERSION: str = '2.0'


def parse_url_from_line(line: str) -> Optional[str]:
    """Parses URL from the line,
    return parsed URL,
    if the line cannot be parsed as a valid URL return None
    """
    striped_line: str = line.strip().split(';', 2)[0]
    if striped_line:
        return striped_line
    return None


def read_infile(infile: TextIO) -> List[str]:
    """
    Reads input file, return a list of URLs
    """
    urls: List[str] = []
    for line in infile:
        url: str = parse_url_from_line(line)
        if url and (url not in urls):
            if url.startswith('http://') or url.startswith('https://'):
                urls.append(url)
            else:
                urls.append(f'https://{url}')
    return urls


def frame_id(index: int) -> str:
    """Get the iframe element id by the index"""
    return f'iframe-{index}'


def iframe_html(index: int, url: str) -> str:
    style: str = f'style="display: block; width: 100%; height: 300px"'
    return f'<iframe id="{frame_id(index)}" src="{url}" {style}></iframe>'


def iframes_html(urls: List[str]) -> str:
    return ''.join(
        [iframe_html(index, url) for index, url in enumerate(urls)]
    )


def get_iframe_urls(driver, index: int, url: str) -> List[str]:
    """Extract a list of valid urls from iframe"""
    urls = []
    wait = WebDriverWait(driver, 30)
    try:
        wait.until(
            expected_conditions.frame_to_be_available_and_switch_to_it(
                (By.ID, frame_id(index))
            )
        )
        urls = driver.execute_script(f"return Array.from(document.querySelectorAll('a[href]')).map(el=>el.href);")
        driver.switch_to.default_content()
        driver.execute_script(
            f'document.getElementById("{frame_id(index)}").parentNode.removeChild(document.getElementById("{frame_id(index)}"))')
    except Exception as e:
        print(f'loading url={url} failed: {e}')
    return urls


def main(patched_stderr: StringIO) -> StringIO:
    start_timestamp: datetime = datetime.now()

    def ts() -> float:
        """Total seconds after start"""
        return (datetime.now() - start_timestamp).total_seconds()

    parser: argparse.ArgumentParser = argparse.ArgumentParser(description='Advanced sites URL collector')
    parser.add_argument('infile', type=argparse.FileType('r'), help='the path to input csv file')
    parser.add_argument('outfile', type=argparse.FileType('w', encoding='UTF-8'), help='the path output csv file')
    parser.add_argument('--version', action='version', version=f'%(prog)s {VERSION}')
    args: argparse.Namespace = parser.parse_args()

    in_urls: List[str] = read_infile(args.infile)
    out_urls: List[str] = []

    chrome_options: Options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    chrome_options.add_argument("--silent")
    chrome_options.add_argument("--headless")
    if not DEBUG:
        chrome_options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get("data:text/html;charset=utf-8,<html></html>")
        driver.execute_script(f'iFrameEls = [];')
        for index, url in enumerate(in_urls):
            driver.execute_script(f'iFrameEl = document.createElement("iframe");')
            driver.execute_script(f'iFrameEl.setAttribute("id", "{frame_id(index)}");')
            driver.execute_script(f'iFrameEl.setAttribute("src", "{url}");')
            driver.execute_script(f'iFrameEl.setAttribute("style", "visibility: hidden");')
            driver.execute_script(f'document.body.appendChild(iFrameEl);')
            driver.execute_script(f'iFrameEl = null;')
            if DEBUG:
                print(f'{ts()} append frame {index}: {url}')
        if DEBUG:
            print(f'{ts()} all frames appended')
    except Exception as e:
        print(f'{ts()} WebDriver GET error: {e}')

    for index, url in enumerate(in_urls):
        urls: List[str] = get_iframe_urls(driver, index, url)
        if DEBUG:
            print(f'{ts()} parsed frame {index}: {url}; found {len(urls)}, total: {len(out_urls)}')
        out_urls += urls

    if DEBUG:
        print(f'{ts()} all frames parsed')
    out_urls = list(set(out_urls))
    if DEBUG:
        print(f'{ts()} all urls unique')

    try:
        driver.close()
    except Exception as e:
        print(f'WebDriver close error: {e}')

    try:
        print('\n'.join(out_urls), file=args.outfile)
    except Exception as e:
        print(f'write to file failed: {e}')
        sys.exit(1)

    try:
        args.outfile.close()
    except Exception as e:
        print(f'Error while closing the outfile handler has occurred: {e}')

    print(f'{ts()} FINISHED total={len(out_urls)} unique urls')
    return patched_stderr


if __name__ == '__main__':
    try:
        errors_io: StringIO = main(StringIO())
        errors: str = errors_io.read()
        if errors:
            print(f'unknown errors: {errors}')
        sys.exit(0)
    except Exception as e_main:
        print(f'Unknown error has occurred in main(): {e_main}')
