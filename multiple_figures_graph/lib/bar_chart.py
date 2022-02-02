from bokeh.io import show, output_file
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource, FactorRange, HoverTool
from bokeh.palettes import Spectral6
from bokeh.plotting import figure


def generate_multi_plot_bar_graph(reports_data, actions, report_file_name):
    plots = []
    output_file(report_file_name)
    for action in actions:
        report_names_and_count, average_time_for_action = extract_average_times_from_reports(reports_data, action)
        source = ColumnDataSource(
            data={
                'report_names_and_count': report_names_and_count,
                'average_time_for_action': average_time_for_action,
                'color': Spectral6
            }
        )
        plot = figure(x_range=FactorRange(*report_names_and_count), active_scroll='wheel_zoom', title=f'Performance Results Comparison - {action}')
        plot.vbar(x='report_names_and_count', top='average_time_for_action', color='color', width=0.9, source=source)
        hover = HoverTool(tooltips=[('Seconds', '@average_time_for_action{0.0[00000000]}')])
        plot.add_tools(hover)
        plots.append(plot)
    main_plot = gridplot([plots])
    show(main_plot)


def extract_average_times_from_reports(reports, action):
    report_names_and_count, average_time_for_action = [], []
    for report in reports:
        report_names_and_count.append(f'{report["report_name"]} - {report["iterations_count"]} iterations')
        average_time_for_action.append(report[action])
    print(report_names_and_count, average_time_for_action)
    return report_names_and_count, average_time_for_action
