from django.contrib import admin
from .models import Categoria, Conteudo, Episodio


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ativo', 'ordem', 'conteudos_count']
    list_editable = ['ativo', 'ordem']
    search_fields = ['nome']
    list_filter = ['ativo']
    
    def conteudos_count(self, obj):
        return obj.conteudos.count()
    conteudos_count.short_description = 'Conteúdos'


@admin.register(Conteudo)
class ConteudoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'categoria', 'ano', 'ativo', 'destaque', 'data_criacao']
    list_editable = ['ativo', 'destaque']
    list_filter = ['tipo', 'categoria', 'ativo', 'destaque', 'ano']
    search_fields = ['titulo', 'descricao']
    readonly_fields = ['data_criacao', 'data_atualizacao']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('titulo', 'descricao', 'tipo', 'categoria')
        }),
        ('Mídia', {
            'fields': ('thumbnail', 'video_url', 'trailer_url')
        }),
        ('Metadados', {
            'fields': ('duracao', 'ano', 'classificacao')
        }),
        ('Status', {
            'fields': ('ativo', 'destaque')
        }),
        ('Timestamps', {
            'fields': ('data_criacao', 'data_atualizacao'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(Episodio) 