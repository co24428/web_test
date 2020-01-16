# test1/urls.py 내용
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
]
