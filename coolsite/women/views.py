from django.shortcuts import render
from django.http import HttpResponse

# Функция представления
def index(request): # ссылка на класс HttpRequest, доступна вся текущая информация в рамках запроса
    return HttpResponse("Страница приложения women")

def categories(request, catid):
    if (request.GET):
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")

def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")












