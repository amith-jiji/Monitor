from django.urls import path
from camera1 import views

urlpatterns = [
    path('', views.indexView, name='index1'),
]
