from django.urls import path
from . import views

urlpatterns = [
    path('', views.membership, name='membership'),
    path('members_only/', views.members_only, name='members_only'),
    path('<article_id>', views.members_articles, name='members_articles'),
    path('health_form', views.health_form, name='health_form'),
    ]
