from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
import test_data


def index(request):
    # template = loader.get_template('prediction/index.html')

    context = {
        'movies': [
            {"id": "id1"},
            {"id": "id2"}
            ],
        'test_data': test_data.print_some_data()
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'prediction/index.html', context)