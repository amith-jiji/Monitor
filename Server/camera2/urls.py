from django.urls import path, include
from camera2 import views

urlpatterns = [
    path('', views.indexView, name='index2'),
]
