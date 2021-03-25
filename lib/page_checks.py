"""
Define page checks.

NOTE:
 - All function sugnatures should be: browser, fqdn, page.
 - Functions implemented here should be added to config_local.py: PAGE_CHECKS['checks'].
"""

from .report_results import add_result


def _prep_row_text(text, page):
    """
    Remove predefined words and format for reporting.
    """
    for i in page['strip_text']:
        text = text.replace(i, '')

    text = " - ".join(text.split('\n'))
    text = " ".join(text.split())

    return text


def chk_status_missing(browser, fqdn, page):
    """
    Check for "Missing from disk!" errors.
    """
    items = browser.find_elements_by_class_name('status-missing')
    for itm in items:
        text = _prep_row_text(itm.text, page)
        add_result(fqdn, text)


def chk_generic_errors(browser, fqdn, page):
    """
    Check for generic errors.
    """
    if browser.current_url != page['final_url']:
        add_result(fqdn, 'Current page ({}), is not the expected page ({})'. \
            format(browser.current_url, page['final_url']))

    items = browser.find_elements_by_class_name('alert')
    for itm in items:
        text = _prep_row_text(itm.text, page)
        add_result(fqdn, text)
