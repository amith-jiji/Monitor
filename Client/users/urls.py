from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginView, name="login"),
    path('logout/', views.logoutView, name="logout"),
    path('dashboard/', views.dashboardView, name="dashboard"),
    path('camera/<int:id>', views.cameraView, name="camera"),
    path('report/<int:id>', views.reportView, name="report"),
]
