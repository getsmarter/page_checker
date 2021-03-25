"""
Config module.
"""
from os import path

# Configure the following in config_local.py. See 'config_local_template.py'.

# Import, parse and validate user's local config in this config file.
try:
    # pylint: disable=unused-import
    from .config_local import PAGE_CHECKS
except ImportError:
    f_path = path.join(path.dirname(__file__), 'config_local.py')
    raise ImportError(f"You need to create a local config file at: {f_path}.")
