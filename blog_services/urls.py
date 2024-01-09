from django.urls import path

from . import views

urlpatterns = [
    path("index/home/", views.index, name="index"),
    path("reporter/", views.ReporterView.as_view(), name="reporter"),
    path("reporter/<int:pk>", views.ReporterDetailView.as_view(), name="reporter"),

]