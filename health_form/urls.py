from django.urls import path
from . import views

urlpatterns = [
    path('', views.health_form, name='health_form'),
    ]