from rest_framework import serializers
from .models import Categoria, Conteudo, Episodio


class EpisodioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episodio
        fields = [
            'id', 'titulo', 'descricao', 'numero', 'temporada', 'thumbnail', 'video_url', 'duracao', 'data_lancamento'
        ]


class CategoriaSerializer(serializers.ModelSerializer):
    conteudos_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Categoria
        fields = ['id', 'nome', 'descricao', 'cor', 'ativo', 'ordem', 'conteudos_count']
    
    def get_conteudos_count(self, obj):
        return obj.conteudos.filter(ativo=True).count()


class ConteudoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    categoria_id = serializers.IntegerField(write_only=True)
    thumbnail_url = serializers.SerializerMethodField()
    episodios = serializers.SerializerMethodField()
    trailer_url = serializers.URLField(required=False, allow_null=True)
    
    class Meta:
        model = Conteudo
        fields = [
            'id', 'titulo', 'descricao', 'tipo', 'categoria', 'categoria_id',
            'thumbnail', 'thumbnail_url', 'video_url', 'trailer_url', 'duracao', 'ano',
            'classificacao', 'ativo', 'destaque', 'data_criacao', 'episodios'
        ]
        read_only_fields = ['data_criacao', 'data_atualizacao']
    
    def get_thumbnail_url(self, obj):
        request = self.context.get('request')
        if obj.thumbnail:
            if request:
                return request.build_absolute_uri(obj.thumbnail.url)
            return obj.thumbnail.url
        return None
    
    def get_episodios(self, obj):
        if obj.tipo == 'serie':
            episodios = obj.episodios.all()
            return EpisodioSerializer(episodios, many=True, context=self.context).data
        return []


class ConteudoListSerializer(serializers.ModelSerializer):
    """Serializer simplificado para listagem"""
    categoria = CategoriaSerializer(read_only=True)
    thumbnail_url = serializers.SerializerMethodField()
    trailer_url = serializers.URLField(required=False, allow_null=True)
    
    class Meta:
        model = Conteudo
        fields = [
            'id', 'titulo', 'tipo', 'categoria', 'thumbnail_url', 'trailer_url',
            'duracao', 'ano', 'classificacao', 'destaque'
        ]
    
    def get_thumbnail_url(self, obj):
        request = self.context.get('request')
        if obj.thumbnail:
            if request:
                return request.build_absolute_uri(obj.thumbnail.url)
            return obj.thumbnail.url
        return None 