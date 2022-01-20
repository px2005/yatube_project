# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Страница со списком
    path('posts/', views.posts_list),
    # Отдельная страница с информацией
    path('posts/<pk>/', views.posts_detail),
    path('group/', views.group),
    path('group/<slug:slug>/', views.group_posts),
]
