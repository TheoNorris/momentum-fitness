from django.urls import path
from . import views

urlpatterns = [
    path('', views.membership, name='membership'),
    path('members_only/', views.members_only, name='members_only'),
    path('members_articles/<article_id>', views.members_articles,
         name='members_articles'),
    ]
