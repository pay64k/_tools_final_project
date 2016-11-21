from django.http import HttpResponse
from django.template import loader



def index(request):
    template = loader.get_template('prediction/index.html')

    context = {
        'movies': [
            {"id": "id1"},
            {"id":"id2"}

            ]

    }
    return HttpResponse(template.render(context, request))
