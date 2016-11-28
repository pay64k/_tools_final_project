from django.http import HttpResponse
import analysis_main as am

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter

import random
import django
import datetime


def sample_graph(request):

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response


# from plotly.graph_objs import Scatter, Layout
# import plotly

# def graph_highest_gross(request):
#
#     print plotly.__version__  # version >1.9.4 required
#     plot = plotly.offline.plot({
#         "data": [
#             Scatter(x=[1, 2, 3, 4], y=[4, 1, 3, 7])
#         ],
#         "layout": Layout(
#             title="hello world"
#         )
#     })
#     return


def graph_highest_gross(request):
    fig=Figure(figsize = (10,20))
    ax=fig.add_subplot(111)

    result = am.find_grossing_movies()

    x=[title for title, gross in result]
    y=[gross for title, gross in result]

    ax.bar(range(0,20),y[:20])
    ax.set_xticklabels(x[:20], rotation='vertical')

    canvas = FigureCanvas(fig)
    response = django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response

