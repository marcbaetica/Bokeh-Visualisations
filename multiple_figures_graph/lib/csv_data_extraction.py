import os
import pandas as pd
from collections import Counter
from pathlib import Path


ACTIONS_COLUMN = 'ACTION_NAME'
AVERAGE_TIME_COLUMN = 'AVERAGE_TIME_IN_SECONDS'
COUNT_COLUMN = 'COUNT'


def read_csv_data_from_reports(folder):
    reports_data = []
    parsed_reports_data = []
    csv_reports_files = os.listdir(folder)
    for report in csv_reports_files:
        reports_data.append(pd.read_csv(str(Path(f'{folder}/{report}'))))
    verify_reports_have_same_actions(reports_data, ACTIONS_COLUMN)
    actions = retrieve_actions_list_from_report(reports_data[0], ACTIONS_COLUMN)
    for report_data, report_name in zip(reports_data, csv_reports_files):
        report_dict = {
            'report_name': report_name.split('.')[0],
            'iterations_count': extract_iterations_count_for_report(report_data)
        }
        for action in actions:
            report_dict[action] = extract_average_time_for_action(action, report_data)
        parsed_reports_data.append(report_dict)
    return parsed_reports_data


def retrieve_actions_list_from_report(report, actions_column):
    verify_column_exists_in_report(report, actions_column)
    return list(report[actions_column])


def extract_average_time_for_action(action, report):
    verify_column_exists_in_report(report, ACTIONS_COLUMN)
    verify_column_exists_in_report(report, AVERAGE_TIME_COLUMN)
    report_df = report[report[ACTIONS_COLUMN] == action]
    return next(report_df.iterrows())[1][AVERAGE_TIME_COLUMN]


def extract_iterations_count_for_report(report):
    verify_column_exists_in_report(report, COUNT_COLUMN)
    return report[COUNT_COLUMN][0]


def verify_reports_have_same_actions(reports_data, actions_column):
    first_report_actions = retrieve_actions_list_from_report(reports_data[0], actions_column)
    for i in range(1, len(reports_data)):
        other_report_actions = retrieve_actions_list_from_report(reports_data[i], actions_column)
        if Counter(first_report_actions) != Counter(other_report_actions):
            raise ValueError('Reports actions do not match. Comparison is not possible.\n'
                             f" One report's actions: {first_report_actions}\n Other report's actions: {other_report_actions}")


def verify_column_exists_in_report(report, column):
    if column not in report.keys():
        raise ValueError(f'Expected column {column} in report.'
                         f' Report contained only columns {list(report.keys())}.')
