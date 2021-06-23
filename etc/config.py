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

PAGE_CHECKS = [
    {
        'url': 'https://berkeley.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://cambridge.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://deloitterise-simmons.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://economist.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://egade-tec-de-monterrey.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://gsb.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://gw.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://harvardbok.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://harvardx.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://imd.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://lse.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://lse2.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://mitcsail.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://mitmedialab.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://mitsap.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://mitsloan.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://northwestern.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://northwesternkellogg.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://oxford.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://ricebusiness.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://sche.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://sdabocconi.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://syracuseischool.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://syracusewhitman.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://ucdavisgsm.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://uchicago.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://uct.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://udayton.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://unc.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://usb.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://wits.onlinecampus.getsmarter.com/admin/plugins.php',
    },
    {
        'url': 'https://yale-som-execed.onlinecampus.getsmarter.com/admin/plugins.php',
    }
]

try:
    # pylint: disable=unused-wildcard-import,wildcard-import
    from .config_local import *
except ImportError:
    f_path = path.join(path.dirname(__file__), 'config_local.py')
    raise ImportError(f"You need to create a local config file at: {f_path}.")
