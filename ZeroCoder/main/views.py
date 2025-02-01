# файл для отображения HTML-шаблонов.
# При получении URL-адреса произойдет переход на какую-либо HTML-страницу.

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data={'caption': 'Cosmos!'}
    return render(request, 'main/index.html', data)

def new(request):
    return render(request, 'main/new.html')

# main/views.py
def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')