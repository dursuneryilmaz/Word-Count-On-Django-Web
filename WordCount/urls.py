from django.conf.urls import url
from .views import *

app_name = 'WordCount'

urlpatterns = [
    url(r'^index/', index, name="index"),
    url(r'^$', index, name="index"),
    url(r'^(?P<idx>\d+)/detail', detail, name="detail"),
    url(r'^create/', create, name="create"),
    url(r'^edit/', edit, name="edit"),
    url(r'^(?P<idx>\d+)/run/', run, name="run"),
    url(r'^(?P<idx>\d+)/delete/', delete, name="delete"),
]
