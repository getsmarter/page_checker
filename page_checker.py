#!/usr/bin/env python
"""
Page Checker - Basic web page checking using Selenium.
"""
import sys

import traceback
import tldextract

from etc import config
from lib import conf_browser, logging, process_url
from lib.report_results import write_report


def main():
    """
    CLI entry point.
    """
    browser = None
    proc_cnt = 0

    try:
        browser = conf_browser()

        total_cnt = len(config.PAGE_CHECKS)

        for page in config.PAGE_CHECKS:
            url = page['url']
            fqdn = tldextract.extract(url).fqdn
            process_url(browser, page, fqdn)

            proc_cnt += 1

            # Print progress information - to be improved.
            sys.stdout.write('\033[2K\033[1G')
            sys.stdout.flush()
            print('({}/{})| {}'.format(proc_cnt, total_cnt, url.partition(fqdn )[2]), end='')
            sys.stdout.flush()

        write_report()

    except Exception as ex:
        logging.error('Exception: %s', ex)
        traceback.print_exc()

    finally:
        if browser:
            browser.quit()


if __name__ == '__main__':
    main()
