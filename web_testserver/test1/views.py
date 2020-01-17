# import 추가
from django.shortcuts import render,redirect
from django.http import HttpResponse
#DB 연결
from django.db import connection
cursor = connection.cursor()

from .models import cctv_data
from .models import user_table

# Create your views here.
# urls에서 만든 이름에 따라 함수 생성
def index(request):
    
    return HttpResponse("<h1>index</h1> page")

def user_insert(request):
    obj = user_table()
    obj.name = "이환"
    obj.cctv_yn = "y"
    obj.small_addr = "김해시"
    obj.big_addr = "경상남도"
    obj.save()

    return HttpResponse("<h1>user_insert</h1> page")
    
def user_bulk_insert(request):
    # bulk_insert
    big_addr = ["서울특별시", "서울특별시"]
    small_addr = ["강남구", "강북구"]
    cctv_no = [2, 0]
    cctv_yn = ["y", 'n']
    objs = []
    for i in range(0, len(cctv_no)):
        obj = user_table()
        obj.cctv_num = cctv_no[i]
        obj.cctv_yn = cctv_yn[i]
        obj.small_addr = small_addr[i]
        obj.big_addr = big_addr[i]
        objs.append(obj)
    # objs.save()
    user_table.objects.bulk_create(objs)

    return HttpResponse("<h1>user_bulk insert</h1>")

def cctv_insert(request):
    obj = cctv_data()
    obj.cctv_num = 30
    obj.cctv_yn = "y"
    obj.small_addr = "김해시"
    obj.big_addr = "경상남도"
    obj.save()

    return HttpResponse("<h1>cctv_insert</h1> page")
    
def cctv_bulk_insert(request):
    # bulk_insert
    big_addr = ["서울특별시", "서울특별시"]
    small_addr = ["강남구", "강북구"]
    cctv_no = [2, 0]
    cctv_yn = ["y", 'n']
    objs = []
    for i in range(0, len(cctv_no)):
        obj = cctv_data()
        obj.cctv_num = cctv_no[i]
        obj.cctv_yn = cctv_yn[i]
        obj.small_addr = small_addr[i]
        obj.big_addr = big_addr[i]
        objs.append(obj)
    # objs.save()
    cctv_data.objects.bulk_create(objs)

    return HttpResponse("<h1>cctv_bulk insert</h1>")
