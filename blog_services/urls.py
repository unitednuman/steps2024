from django.urls import path

from . import views

urlpatterns = [
    path("index/home/", views.index, name="index"),
]