from django.urls import path
from . import views

# присваеваем имена адресам страниц
urlpatterns = [
    path('', views.home, name='news_home'), # добавляем имя страницы
]