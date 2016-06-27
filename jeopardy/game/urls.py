
from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^(?P<air_date>\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01]))/$', views.date, name='date'),
]