from . import views
from django.urls import path


urlpatterns = [
    path( "homepage/", views.home)
]
