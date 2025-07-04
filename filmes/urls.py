from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, ConteudoViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'conteudos', ConteudoViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 