from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home_about/', views.home_about, name='home_about'),
    ]

