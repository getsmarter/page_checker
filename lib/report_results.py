"""
Manage reporting.
"""
import csv
import datetime

PLUGIN_RESULTS_HEADER = ['FQDN', 'Plugin Name', 'Plugin Detail', 'Version', 'Message']
GENERAL_MESSAGE_HEADER = ['FQDN', 'Message']

_plugin_report_results = []
_general_report_results = []

def add_plugin_report_result(plugin_name, plugin_detail, version, message, fqdn):
    """
    Add a plugin report record.
    """
    _plugin_report_results.append({
        'Plugin Name': plugin_name,
        'Plugin Detail': plugin_detail,
        'Version': version,
        'Message': message,
        'FQDN': fqdn,
    })


def add_general_report_result(fqdn, message):
    """
    Add a general report record.
    """
    _general_report_results.append({
        'FQDN': fqdn,
        'Message': message
    })


def write_reports():
    """
    Serialise reports.
    """
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')

    if _plugin_report_results:
        file_name = 'var/plugin_results_{}.csv'.format(timestamp)
        with open(file_name, 'w') as f_out:
            writer = csv.DictWriter(f_out, fieldnames=PLUGIN_RESULTS_HEADER)
            writer.writeheader()
            writer.writerows(_plugin_report_results)

    if _general_report_results:
        file_name = 'var/general_messages_{}.csv'.format(timestamp)
        with open(file_name, 'w') as f_out:
            writer = csv.DictWriter(f_out, fieldnames=GENERAL_MESSAGE_HEADER)
            writer.writeheader()
            writer.writerows(_general_report_results)
