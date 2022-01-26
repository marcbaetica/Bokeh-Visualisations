# python results_comparison.py samples/results1.csv samples/results2.csv

import sys
from lib.bar_chart import generate_multi_plot_bar_graph
from lib.data_extraction import read_csv_data_from_files
from pprintpp import pprint


REPORT_1 = sys.argv[1]
REPORT_2 = sys.argv[2]

x, y = read_csv_data_from_files(REPORT_1, REPORT_2)
generate_multi_plot_bar_graph(x, y)
