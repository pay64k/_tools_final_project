from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Main Page</h1>"
                        "<a href='prediction'>Go to prediction</a>"
                        "</br>"
                        "<a href='analysis'>Go to analysis</a>")