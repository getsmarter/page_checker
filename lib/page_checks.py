"""
Check page for the presence of specified classes.
"""

from etc import config
from .report_results import add_general_report_result, add_plugin_report_result


def _prep_row_text(text, strip_text):
    """
    Remove predefined words and format for reporting.
    """
    for i in strip_text:
        text = text.replace(i, '')

    items = text.split('\n')

    return [itm.strip() for itm in items]


def _process_checks(browser, check_classes, strip_text):
    """
    Process rules for the page.
    """
    for class_item in check_classes:
        class_item_results = browser.find_elements_by_class_name(class_item)
        for itm in class_item_results:
            res = _prep_row_text(itm.text, strip_text)
            if len(res) > 4:
                plugin_msg = res[:4]
                add_plugin_report_result(*plugin_msg + [browser.current_url])
                other_msg = res[4:]
                add_general_report_result(browser.current_url, ''.join(other_msg))
            elif len(res) != 4:
                add_general_report_result(browser.current_url, ''.join(res))
            elif class_item == 'status-missing':
                add_plugin_report_result(*res + [browser.current_url])
            else:
                add_general_report_result(browser.current_url, ''.join(res))


def chk_page(browser, page):
    """
    Check the page for elements to indicate potential issues.
    """
    # Confirm that we are on the intended page.
    expected_url = page.get('expected_url', page['url'])
    if browser.current_url != expected_url:
        add_general_report_result(browser.current_url, '{}, expected: {}'.format(browser.current_url, expected_url))

    # Iterate through all checks.
    page_check_items = page.get('page_check_items', config.PAGE_CHECK_ITEMS)
    for check_item in page_check_items:
        check_classes = check_item.get('class', [])
        strip_text = check_item.get('strip_text', [])
        _process_checks(browser, check_classes, strip_text)
