# python results_comparison.py samples/results1.csv samples/results2.csv

import sys
from lib import read_csv_data_from_files
from pprintpp import pprint


pprint(sys.argv)
REPORT_1 = sys.argv[1]
REPORT_2 = sys.argv[2]


read_csv_data_from_files(REPORT_1, REPORT_2)
