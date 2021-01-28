"""
This type stub file was generated by pyright.
"""

import argparse
from argparse import RawDescriptionHelpFormatter
from seleniumwire.proxy import utils

def standalone_proxy(port=...):
    ...

if __name__ == '__main__':
    commands = { 'extractcert': utils.extract_cert,'standaloneproxy': standalone_proxy }
    parser = argparse.ArgumentParser(description='\n\nsupported commands: \n  %s' % '\n  '.join(sorted(commands)), formatter_class=RawDescriptionHelpFormatter, usage='python -m seleniumwire <command>')
    args = parser.parse_args()
    pargs = [arg for arg in args.args if '=' not in arg and arg is not args.command]
    kwargs = dict([tuple(arg.split('=')) for arg in args.args if '=' in arg])
