from django.conf.urls import url
from . import views
import graphs

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^graphs/sample.png$', graphs.sample_graph),
    url(r'^graphs/gross.png$', graphs.graph_highest_gross),
]