from django.urls import path
from camera2 import views

urlpatterns = [
    path('', views.indexView, name='index2'),
]
