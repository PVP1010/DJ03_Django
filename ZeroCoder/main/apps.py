#  файл с настройками, но не общими, а для конкретного приложения main;

from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
