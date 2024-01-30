from django.contrib import admin
from django.urls import path
from recipes.views import home, contato, sobre


urlpatterns = [
    path('sobre/', sobre),  # /sobre/
    path('contato/', contato),  # /contato/
    path('', home),  # home
]
