from django.contrib import admin
from django.urls import path, include #include 추가
from videoApp.views import home # videoApp에 있는 모든 함수를 가져온다. -> home으로 변경

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = "home"),                    # path('url 주소', views.py에 있는 함수명, name =  "namespace" html에서 접근가능한 이름 지정)
    path('videoApp/', include('videoApp.urls')),  
    
    # path('main/',mainVideo, name = "mainVideo"),
    # path('<str:id>', detailVideo, name="detailVideo"), # '<str:id>' 는 path converter
    # path('new/',newVideo,name="newVideo"), 
    # path('create/', createVideo, name="createVideo"),
    # path('edit/<str:id>',editVideo, name = "editVideo"),
    # path('update/<str:id>',updateVideo,name = "updateVideo"),
    # path('delete/<str:id>', deleteVideo, name = "deleteVideo"),
]