# test1/urls.py 내용
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index"),
    path('cctv_insert', views.cctv_insert, name="cctv_insert"),
    path('cctv_bulk_insert', views.cctv_bulk_insert, name="cctv_bulk_insert"),
]
