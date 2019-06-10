from django.urls import path

from .views import *

urlpatterns = [
    path('', glav, name='glav_url'),
    path('sovr_proza/', sovr_proza, name='sovr_proza_url'),
    path('biograph/', biograph, name='biograph_url'),
    path('comics/', comics, name='comics_url'),
]