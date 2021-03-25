"""
Initialization file for library module.
"""
import logging

import requests

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from etc import config
from .report_results import add_result
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


def process_url(browser, page, fqdn):
    """
    Process a single page.
    """
    browser.delete_all_cookies()

    loaded_ok = load(browser, page['url'])
    if not loaded_ok:
        add_result(fqdn, 'Selenium could not load page.')
        return

    if page['url_login_path'] in browser.current_url:
        browser.find_element_by_id('username').send_keys(page['username'])
        browser.find_element_by_id('password').send_keys(page['password'])
        browser.find_element_by_id('loginbtn').click()

    for check in page['checks']:
        globals()[check](browser, fqdn, page)
