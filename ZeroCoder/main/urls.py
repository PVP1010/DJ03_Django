from django.urls import path
from . import views

# присваеваем имена адресам страниц
urlpatterns = [
    path('', views.index, name='home'), # добавляем имя страницы home
    path('new/', views.new, name='page2'), # добавляем имя страницы page2
]