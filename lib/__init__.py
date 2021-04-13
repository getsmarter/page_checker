"""
Initialization file for library module.
"""
import logging

import requests

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from etc import config
from .report_results import add_report_result
from .page_checks import *

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.WARN)


HEADLESS = True
WAIT_S = 20


def conf_browser():
    """
    Configure the browser instance.
    """
    ff_options = FirefoxOptions()
    ff_options.headless = HEADLESS

    browser = webdriver.Firefox(options=ff_options)
    browser.implicitly_wait(WAIT_S)

    return browser


def load(browser, url):
    """
    Load the page into the browser instance.
    """
    loaded_ok = False

    try:
        browser.get(url)
    except TimeoutException:
        logging.error('TimeoutException: Error loading: %s', url)
    except requests.exceptions.RequestException:
        logging.error('RequestException: Error loading: %s', url)
    except Exception:
        logging.error('Exception: Error loading: %s', url)
    else:
        loaded_ok = True

    return loaded_ok


def process_url(browser, page):
    """
    Process a single page.
    """
    # Clear authentication cookies.
    browser.delete_all_cookies()

    loaded_ok = load(browser, page['url'])
    if not loaded_ok:
        add_report_result(page['url'], 'Could not load page.')
        return

    # Login, if needed.
    login_page_url = page.get('login_page_url', config.PC_LOGIN_PAGE_URL)
    login_field_username = page.get('login_field_username', config.LOGIN_FIELD_USERNAME)
    login_field_password = page.get('login_field_password', config.LOGIN_FIELD_PASSWORD)
    login_button = page.get('login_button', config.LOGIN_BUTTON)

    if login_page_url and login_page_url in browser.current_url:
        browser.find_element_by_id(login_field_username).send_keys(page.get('username', config.PC_USERNAME))
        browser.find_element_by_id(login_field_password).send_keys(page.get('password', config.PC_PASSWORD))
        browser.find_element_by_id(login_button).click()

    # Run checks.
    chk_page(browser, page)
