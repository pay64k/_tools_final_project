from django.http import HttpResponse

def index(requset):
    return HttpResponse("<h1>Prediction Page")