"""
Notes:
- This is the main configuration file.
- Default config values defined below.
- Override values below in 'config_local.py'
- See 'config_local_template' for variable documentation.
"""

from os import path

PC_LOGIN_PAGE_URL = '/login/index.php'

LOGIN_FIELD_USERNAME = 'username'
LOGIN_FIELD_PASSWORD = 'password'
LOGIN_BUTTON = 'loginbtn'

DELETE_COOKIES = True

PAGE_CHECK_ITEMS = [
    {
        'class': ['alert', 'status-missing'],
        'strip_text': ['Uninstall', 'Settings', 'Disabled', 'Additional']
    }
]


try:
    # pylint: disable=unused-wildcard-import,wildcard-import
    from .config_local import *
except ImportError:
    f_path = path.join(path.dirname(__file__), 'config_local.py')
    raise ImportError(f"You need to create a local config file at: {f_path}.")
