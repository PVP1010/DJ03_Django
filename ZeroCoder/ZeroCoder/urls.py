from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')),                         # добавляем ссылку на наш  файл news
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # добавляем ссылку на наш статический файл
