from django.urls import path
from feed import views

urlpatterns = [
    path('', views.indexView, name='index'),
]
