import sys
from lib.bar_chart import generate_multi_plot_bar_graph
from lib.csv_data_extraction import parse_data_from_csv_reports
from pprintpp import pprint


try:
    REPORTS_FOLDER = sys.argv[1]
except IndexError:
    print('Invalid parameter input. Missing location of reports folder.'
          ' Example: python generate_reports_graph.py samples')
    sys.exit(1)

reports_data, actions = parse_data_from_csv_reports(REPORTS_FOLDER)
generate_multi_plot_bar_graph(reports_data, actions, 'performance_per_action_report_graph.html')
