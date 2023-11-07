from django.urls import path
from . import views

urlpatterns = [
    path("get", views.get_off, name="get-off"),
    path("set", views.set_off, name="set-off"),
    path("getg", views.get_offg, name="get-offg"),
    path("setg", views.set_offg, name="set-offg"),
]
