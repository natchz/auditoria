from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$', index, name="inicio"),
	url(r'^diagrama/$', graph, name="graph"),
]
