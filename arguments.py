"""
arguments.py

Author: shmakovpn <shmakovpn@yandex.ru>
Date: 2021-01-14
"""
import argparse


def get_arguments() -> argparse.Namespace:
    """Processing command line arguments"""
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description='Advanced sites URL collector')
    parser.add_argument('infile', type=argparse.FileType('r'), help='the path to input csv file')
    parser.add_argument('outfile', type=argparse.FileType('w', encoding='UTF-8'), help='the path output csv file')
    parser.add_argument('--version', action='version', version=f'%(prog)s {VERSION}')
    args: argparse.Namespace = parser.parse_args()
