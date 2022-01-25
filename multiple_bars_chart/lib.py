import pandas as pd
from pprintpp import pprint


def read_csv_data_from_files(report_1, report_2):
    x, y = [], []
    actions_column = 'ACTION_NAME'
    average_time_column = 'AVERAGE_TIME_IN_SECONDS'
    report_1_data = pd.read_csv(report_1)
    report_2_data = pd.read_csv(report_2)
    actions_report_1 = retrieve_actions_list_from_report(report_1_data, actions_column)
    actions_report_2 = retrieve_actions_list_from_report(report_2_data, actions_column)
    verify_reports_have_same_actions(actions_report_1, actions_report_2)
    for action in actions_report_1:
        # TODO: compress this into 1 set of calls.
        x.append((action, '1'))
        y.append(extract_average_time_for_action(action, actions_column, report_1_data, average_time_column))
        x.append((action, '2'))
        y.append(extract_average_time_for_action(action, actions_column, report_2_data, average_time_column))

def retrieve_actions_list_from_report(report, actions_column):
    if actions_column not in report.keys():
        raise ValueError(f'Expected column {actions_column} in report.'
                         f' Report contained only columns {list(report.keys())}.')
    return list(report[actions_column])


def verify_reports_have_same_actions(actions_report_1, actions_report_2):
    if actions_report_1 != actions_report_2:
        raise ValueError('The two reports have different actions. Comparison is not possible.\n'
                         f' Report 1 actions: {actions_report_1}\n Report 2 actions: {actions_report_2}')


def extract_average_time_for_action(action, actions_column, report_df, average_time_column):
    report_df = report_df[report_df[actions_column] == action]
    pprint(list(report_df.iterrows()))
    pprint(next(report_df.iterrows())[1][average_time_column])
    print()