"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from learn import views as learn_views  # new
#�������ҳ����ת1
# urlpatterns = [
#     path('', learn_views.home),  # new
#    path('add/<int:a>/<int:b>/', learn_views.add, name='add'),
#    path('add/', learn_views.add2, name='add2'),
#     path('admin/', admin.site.urls),
# ]
#ģ��̳�2
# urlpatterns = [
#     path('', learn_views.home),  # new
#     path('admin/', admin.site.urls),
# ]

#ģ�����
# urlpatterns = [
#     path('', learn_views.home),  # new
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    path('', learn_views.index),  # new
   path('add/', learn_views.add, name='add'),
    path('admin/', admin.site.urls),
]


