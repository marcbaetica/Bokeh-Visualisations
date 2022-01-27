import pandas as pd
from collections import Counter


def read_csv_data_from_files(report_1, report_2):
    x, y = [], []
    actions_column = 'ACTION_NAME'
    average_time_column = 'AVERAGE_TIME_IN_SECONDS'
    report_1_data = pd.read_csv(report_1)
    report_2_data = pd.read_csv(report_2)
    verify_reports_have_same_actions(report_1_data, report_2_data, actions_column)
    for report_number in range(1, 3):
        for action in retrieve_actions_list_from_report(report_1_data, actions_column):
            x.append((action, str(report_number)))
            y.append(extract_average_time_for_action(action, actions_column, eval(f'report_{report_number}_data'), average_time_column))
    return x, y


def retrieve_actions_list_from_report(report, actions_column):
    verify_column_exists_in_report(report, actions_column)
    return list(report[actions_column])


def extract_average_time_for_action(action, actions_column, report, average_time_column):
    verify_column_exists_in_report(report, actions_column)
    verify_column_exists_in_report(report, average_time_column)
    report_df = report[report[actions_column] == action]
    return next(report_df.iterrows())[1][average_time_column]


def verify_reports_have_same_actions(report_1_data, report_2_data, actions_column):
    actions_report_1 = retrieve_actions_list_from_report(report_1_data, actions_column)
    actions_report_2 = retrieve_actions_list_from_report(report_2_data, actions_column)
    if Counter(actions_report_1) != Counter(actions_report_2):
        raise ValueError('The two reports have different actions. Comparison is not possible.\n'
                         f' Report 1 actions: {actions_report_1}\n Report 2 actions: {actions_report_2}')


def verify_column_exists_in_report(report, column):
    if column not in report.keys():
        raise ValueError(f'Expected column {column} in report.'
                         f' Report contained only columns {list(report.keys())}.')
