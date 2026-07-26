from django.urls import path

from greetings.views import home


urlpatterns = [
    path("", home, name="home"),
]
