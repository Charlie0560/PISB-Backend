import django.urls
from django.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path("number/", views.number, name="number"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("showusername/", views.showusername, name="showusername"),
    path("numprint/", views.numprint, name="numprint"),
    path("showusername/numprint/", views.numprint, name="numprint"),
]