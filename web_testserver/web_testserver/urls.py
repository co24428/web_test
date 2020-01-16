
from django.contrib import admin
# import에 include 추가
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # urlpatterns에 추가
    path('test1/', include('test1.urls')),
]
