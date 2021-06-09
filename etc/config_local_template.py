"""
Configuration file template.

Copy file and name it 'config_local.py'. This file is unversioned.
"""

# Default login page field names.
LOGIN_FIELD_USERNAME = 'username'
LOGIN_FIELD_PASSWORD = 'password'
LOGIN_BUTTON = 'loginbtn'

## Defaults for PAGE_CHECKS attribute values.
# The default login page.
PC_LOGIN_PAGE_URL = '/login/index.php'
# Default username & password.
PC_USERNAME = None
PC_PASSWORD = None

DELETE_COOKIES = True

# Default checks, can be overridden per URL.
PAGE_CHECK_ITEMS = [
    {
        # List of class names to check for.
        'class': [],
        # List of text to remove.
        'strip_text': []
    }
]

# Pages to check, based on the following:
"""
    PAGE_CHECKS - a list of processing instruction dictionaries.

    Keys:
    ----------
    url: str
        - The URL to test.
        - Required.

    expected_url: str
        - Indicate the url redirected to as a result of processing the page.
        - Optional.
        - If not present, 'url' used.

    login_page_url: str
        - The url to the login page.
        - Optional (Required if user authentication required).
        - PC_LOGIN_PAGE_URL: Default value.
    login_field_username: str
        - Name of the 'username' field.
        - Optional (Required if user authentication required).
        - LOGIN_FIELD_USERNAME: Default value.
    login_field_password: str
        - Name of the 'password' field.
        - Optional (Required if user authentication required).
        - LOGIN_FIELD_PASSWORD: Default value.
    login_button: str
        - Name of the 'login' button.
        - Optional (Required if user authentication required).
        - LOGIN_BUTTON: Default value.

    username: str
        - Username to use for this 'url', if authentication required.
        - Optional (Required if user authentication required).
        - LOGIN_FIELD_USERNAME: Default value.
    password: str
        - Password to use for this 'url', if authentication required.
        - Optional (Required if user authentication required).
        - PC_PASSWORD: Default value.

    page_check_items: list of dictionaries
        - Check page using specific rule set, use structure of PAGE_CHECK_ITEMS.
        - Optional.
        - PAGE_CHECK_ITEMS: Default value.

    delete_ccokies: boolean
        - Determine if cookies for this check should be cleared.
        - Optional.
        - delete_cookies: Default value.
"""
PAGE_CHECKS = [
    {
        'url': str,
        # ...
    },
]
