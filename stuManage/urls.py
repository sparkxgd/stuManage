"""stuManage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from stu import views
from stu.controller import schoolController
from stu.controller import classinfoController
from stu.controller import userController
from stu.controller import uploadCotroller

urlpatterns = [
    path('admin/', admin.site.urls),
    path('openlogin/', views.openlogin),
    path('login/', views.login),
    path('login_face/', views.login_face),
    path('logout/', views.logout),
    path('index/', views.index),
    path('get_session/', views.get_session),
    path('school/', include([
        path('list/', schoolController.getlist),
        path('add/', schoolController.add),
        path('edit/', schoolController.edit),
        path('delete/', schoolController.delete),
        path('batchdel/', schoolController.batchdel),
    ])),
    path('class/', include([
            path('list/', classinfoController.getlist),
            path('add/', classinfoController.add),
            path('edit/', classinfoController.edit),
            path('delete/', classinfoController.delete),
            path('batchdel/', classinfoController.batchdel),
        ])),
    path('user/', include([
            path('list/', userController.getlist),
            path('add/', userController.add),
            path('edit/', userController.edit),
            path('delete/', userController.delete),
            path('batchdel/', userController.batchdel),
        ])),
    path('upload/', include([
        path('upload_face_detect/', uploadCotroller.upload_face_detect),
        path('face_detect/', uploadCotroller.face_detect),
        path('face_match/', uploadCotroller.face_match),
        path('face_detect_base_login/', uploadCotroller.face_detect_base_json),
    ])),


]
