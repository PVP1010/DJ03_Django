from django.shortcuts import render, redirect                            # импортируем функцию render и функцию redirect
from .models import News_post                                  # импортируем модель News_post
from .forms import News_postForm                                # импортируем форму
# Create your views here.

def home(request):
    news = News_post.objects.all()             # берём все объекты из класса News_post и сохраняем в переменную news
    return render(request, 'news/news.html', {'news': news})  # передаем их в виде словаря news.

def create_news(request):
    error = ''
    if request.method == 'POST':
        form = News_postForm(request.POST)
        if form.is_valid():
            form.save()                                      # сохраняем новость
            return redirect('news_home')                     # перенаправляем на главную страницу
        else:
            error = "Данные были заполнены некорректно"
    form = News_postForm()
    return render(request, 'news/add_new_post.html', {'form': form, 'error': error})