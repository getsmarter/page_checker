"""
Manage reporting.
"""
import csv
import datetime

REPORT_RESULTS_HEADER = ['fqdn', 'message']

_report_results = []

def add_report_result(fqdn, message):
    """
    Add a report record.
    """
    if fqdn and message:
        _report_results.append({
            'fqdn': fqdn,
            'message': message
        })


def write_report():
    """
    Serialise report.
    """
    file_name = 'var/{}_{}.csv'.format('errors_', datetime.datetime.now().strftime('%Y-%m-%d_%H-%M'))

    with open(file_name, 'w') as f_out:
        writer = csv.DictWriter(f_out, fieldnames=REPORT_RESULTS_HEADER)
        writer.writeheader()
        writer.writerows(_report_results)
