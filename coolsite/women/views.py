from django.shortcuts import render
from django.http import HttpResponse

# Функция представления
def index(request): # ссылка на класс HttpRequest, доступна вся текущая информация в рамках запроса
    return HttpResponse("Страница приложения women")

def categories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")