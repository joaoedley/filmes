"""
URL configuration for filmeapp project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('filmes.urls')),
]

# Serve media files in all environments (necessário para Render Free)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 