from django.http import HttpResponse
from django.shortcuts import render

import analysis_main

def index(request):


    context = {
        'movies': [
            {"id": "id1"},
            {"id": "id2"}
            ],
        'data1': analysis_main.prediction.dummy_data
    }
    return render(request, 'analysis/index.html', context)

    # return HttpResponse("<h1>Analysis Page</h1>")

