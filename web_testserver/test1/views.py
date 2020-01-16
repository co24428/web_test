# import 추가
from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
# urls에서 만든 이름에 따라 함수 생성
def index(request):
    return HttpResponse("This is index page")