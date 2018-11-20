from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
