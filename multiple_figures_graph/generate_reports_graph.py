import sys
from lib.csv_data_extraction import read_csv_data_from_reports
from pprintpp import pprint


try:
    REPORTS_FOLDER = sys.argv[1]
except IndexError:
    print('Invalid parameter input. Missing location of reports folder.'
          ' Example: python generate_reports_graph.py samples')
    sys.exit(1)

reports_data = read_csv_data_from_reports(REPORTS_FOLDER)
pprint(reports_data)
