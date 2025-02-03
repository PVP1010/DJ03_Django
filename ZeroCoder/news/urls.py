from django.urls import path
from . import views

# присваеваем имена адресам страниц
urlpatterns = [
    path('', views.home, name='news_home'),                        # добавляем имя страницы
    path('create_news/', views.create_news, name='add_news'),      # добавляем имя страницы add_news
]

