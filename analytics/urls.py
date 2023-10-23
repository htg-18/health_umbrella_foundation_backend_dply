from django.urls import path
from . import views

urlpatterns = [
    path("get", views.get_off, name="get-off"),
    path("set", views.set_off, name="set-off"),
]
