from django.urls import path

from . import views

urlpatterns = [
    path("", views.number, name="number"),
    path("numprint/", views.numprint, name="numprint"),
    path("number/", views.number, name="number")
]
