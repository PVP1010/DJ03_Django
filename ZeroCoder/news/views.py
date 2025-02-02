from django.shortcuts import render
from .models import News_post                                  # импортируем модель News_post
# Create your views here.

def home(request):
    news = News_post.objects.all()                                                # получаем все новости из базы данных
    return render(request, 'news/news.html', {'news': news})  # передаем новости в шаблон сайта news.
