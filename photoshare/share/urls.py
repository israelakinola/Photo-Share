"""Share App URL Configuration """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ="share.home"),
]
