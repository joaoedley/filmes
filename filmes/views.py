from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Categoria, Conteudo
from .serializers import (
    CategoriaSerializer, ConteudoSerializer, ConteudoListSerializer
)


class CategoriaViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet para categorias"""
    queryset = Categoria.objects.filter(ativo=True)
    serializer_class = CategoriaSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['ativo']
    ordering_fields = ['ordem', 'nome']
    ordering = ['ordem', 'nome']
    
    @action(detail=True, methods=['get'])
    def conteudos(self, request, pk=None):
        """Retorna os conteúdos de uma categoria específica"""
        categoria = self.get_object()
        conteudos = categoria.conteudos.filter(ativo=True)
        
        # Filtros opcionais
        tipo = request.query_params.get('tipo')
        if tipo:
            conteudos = conteudos.filter(tipo=tipo)
        
        destaque = request.query_params.get('destaque')
        if destaque:
            conteudos = conteudos.filter(destaque=destaque.lower() == 'true')
        
        serializer = ConteudoListSerializer(conteudos, many=True, context={'request': request})
        return Response(serializer.data)


class ConteudoViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet para conteúdos (filmes e séries)"""
    queryset = Conteudo.objects.filter(ativo=True)
    serializer_class = ConteudoListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['tipo', 'categoria', 'destaque', 'ano']
    search_fields = ['titulo', 'descricao']
    ordering_fields = ['titulo', 'data_criacao', 'ano']
    ordering = ['-data_criacao']
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ConteudoSerializer
        return ConteudoListSerializer
    
    @action(detail=False, methods=['get'])
    def destaques(self, request):
        """Retorna os conteúdos em destaque"""
        destaques = self.queryset.filter(destaque=True)
        serializer = self.get_serializer(destaques, many=True, context={'request': request})
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def recentes(self, request):
        """Retorna os conteúdos mais recentes"""
        limit = int(request.query_params.get('limit', 10))
        recentes = self.queryset.order_by('-data_criacao')[:limit]
        serializer = self.get_serializer(recentes, many=True, context={'request': request})
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def por_tipo(self, request):
        """Retorna conteúdos filtrados por tipo (filme/série)"""
        tipo = request.query_params.get('tipo')
        if not tipo or tipo not in ['filme', 'serie']:
            return Response(
                {'error': 'Tipo deve ser "filme" ou "serie"'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        conteudos = self.queryset.filter(tipo=tipo)
        serializer = self.get_serializer(conteudos, many=True, context={'request': request})
        return Response(serializer.data) 