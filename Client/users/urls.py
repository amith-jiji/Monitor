from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.loginView, name="login"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('camera/<int:id>',views.cameraView,name="camera"),
    path('report/<int:id>',views.reportView,name="report"),
    path('logout/', views.logout, name="log"),
]
