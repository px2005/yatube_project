# posts/urls.py
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
    # Страница со списком
    path('posts/', views.posts_list, name='posts_list'),
    # Отдельная страница с информацией
    # path('posts/<pk>/', views.posts_detail),
    path('group/', views.group_posts, name='group'),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
]
