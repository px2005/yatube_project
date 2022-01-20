from django.shortcuts import render

# Create your views here.
# posts/views.py
from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Главная страница')


# Страница со списком мороженого
def posts_list(request):
    return HttpResponse('Список мороженого')


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def posts_detail(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')

def group(request):
    return HttpResponse('Список group')

def group_posts(request, slug):
    return HttpResponse(f'group_posts {slug}')
