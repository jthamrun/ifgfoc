from django.urls import path

from . import views

app_name = 'ifgfoc'

urlpatterns = [
    path("", views.index, name="index"),
    path("about-us", views.aboutUs, name="aboutUs"),
    path("give", views.give, name="give"),
    path("care-group", views.caregroup, name="care-group"),
    path("stream", views.stream, name="stream"),
    path("connect-card", views.connectcard, name="connect-card")
]