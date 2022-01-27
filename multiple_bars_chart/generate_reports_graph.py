# python generate_reports_graph.py samples/report_1.csv samples/report_2.csv

import sys
from lib.bar_chart import generate_multi_plot_bar_graph
from lib.data_extraction import read_csv_data_from_files


try:
    REPORT_1 = sys.argv[1]
    REPORT_2 = sys.argv[2]
except IndexError:
    print('Invalid parameter input. Missing location of reports to compare.'
          ' Example: python generate_reports_graph.py samples/report_1.csv samples/report_2.csv')
    sys.exit(1)

x, y = read_csv_data_from_files(REPORT_1, REPORT_2)
generate_multi_plot_bar_graph(x, y, 'report_graph.html')
