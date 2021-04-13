"""
Config module. Import local configuration file.
"""
from os import path


try:
    # pylint: disable=unused-import,disable=unused-wildcard-import,wildcard-import
    from .config_local import *
except ImportError:
    f_path = path.join(path.dirname(__file__), 'config_local.py')
    raise ImportError(f"You need to create a local config file at: {f_path}.")
