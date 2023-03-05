from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404



# Функция представления
def index(request): # ссылка на класс HttpRequest, доступна вся текущая информация в рамках запроса
    return render(request, 'women/index.html/')






def categories(request, catid):
    if (request.GET):
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2023:
        return redirect("home", permanent=False)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")










