"""
This type stub file was generated by pyright.
"""

import logging

LOGGER = logging.getLogger(__name__)
def format_json(json_struct):
    ...

def dump_json(json_struct):
    ...

def load_json(s):
    ...

def unzip_to_temp_dir(zip_file_name):
    """Unzip zipfile to a temporary directory.

    The directory of the unzipped files is returned if success,
    otherwise None is returned. """
    ...
