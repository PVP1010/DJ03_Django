from django.shortcuts import render
from .models import News_post                                  # импортируем модель News_post
# Create your views here.

def home(request):
    news = News_post.objects.all()             # берём все объекты из класса News_post и сохраняем в переменную news
    return render(request, 'news/news.html', {'news': news})  # передаем их в виде словаря news.
