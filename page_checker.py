#!/usr/bin/env python
"""
Page Checker - Basic web page checking using Selenium.
"""
from datetime import datetime
import sys
import traceback
import tldextract

from etc import config
from lib import conf_browser, logging, process_url
from lib.report_results import write_reports


def main():
    """
    CLI entry point.
    """
    browser = None
    proc_cnt = 0

    try:
        browser = conf_browser()

        total_cnt = len(config.PAGE_CHECKS)

        checks_start = datetime.now()
        print('Starting checks: {}'.format(checks_start.strftime("%Y-%m-%d %H:%M:%S")))

        for page in config.PAGE_CHECKS:
            url = page['url']
            fqdn = tldextract.extract(url).fqdn

            if proc_cnt > 0:
                # Back to previous line.
                sys.stdout.write("\033[F")
                # Clear line.
                sys.stdout.write("\033[K")
            print('{} - ({}/{}) > {}'.format(fqdn, proc_cnt, total_cnt, url.partition(fqdn )[2]))

            process_url(browser, page)
            proc_cnt += 1

        write_reports()

        checks_complete = datetime.now()
        duration = checks_complete - checks_start
        minutes, seconds = divmod(duration.seconds, 60)

        print('Completed: {} - {}.{} minutes.'.format(checks_complete.strftime("%Y-%m-%d %H:%M:%S"), minutes, seconds))
        print("All checks are done. Please review /var for results")

    except Exception as ex:
        logging.error('Exception: %s', ex)
        traceback.print_exc()

    finally:
        if browser:
            browser.quit()


if __name__ == '__main__':
    main()
