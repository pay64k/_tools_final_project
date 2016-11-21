from django.conf.urls import url
from . import views

urlpatterns = [
    # /prediction/
    url(r'^$', views.index, name='index'),
]