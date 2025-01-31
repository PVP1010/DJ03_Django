# файл для отображения HTML-шаблонов.
# При получении URL-адреса произойдет переход на какую-либо HTML-страницу.

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")

def new(request):
    return HttpResponse("<h1>Это вторая страница на Django</h1>")