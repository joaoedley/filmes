from django.db import models


class Categoria(models.Model):
    """Modelo para categorias de filmes e séries"""
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    cor = models.CharField(max_length=7, default='#FF6B6B', help_text='Cor em formato hexadecimal')
    ativo = models.BooleanField(default=True)
    ordem = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['ordem', 'nome']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.nome


class Conteudo(models.Model):
    """Modelo para filmes e séries"""
    TIPO_CHOICES = [
        ('filme', 'Filme'),
        ('serie', 'Série'),
    ]
    
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='filme')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='conteudos')
    
    # Thumbnail
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    
    # Vídeo (Bunny.net)
    video_url = models.URLField(help_text='URL do vídeo no Bunny.net')
    trailer_url = models.URLField(blank=True, null=True, help_text='URL do trailer (opcional)')
    
    # Metadados
    duracao = models.CharField(max_length=20, blank=True, help_text='Ex: 2h 15min')
    ano = models.IntegerField(blank=True, null=True)
    classificacao = models.CharField(max_length=10, blank=True, help_text='Ex: 12, 16, 18')
    
    # Status
    ativo = models.BooleanField(default=True)
    destaque = models.BooleanField(default=False, help_text='Aparecer nos destaques')
    
    # Timestamps
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-data_criacao']
        verbose_name = 'Conteúdo'
        verbose_name_plural = 'Conteúdos'
    
    def __str__(self):
        return f"{self.titulo} ({self.get_tipo_display()})"
    
    @property
    def thumbnail_url(self):
        """Retorna a URL completa da thumbnail"""
        if self.thumbnail:
            return self.thumbnail.url
        return None 


class Episodio(models.Model):
    conteudo = models.ForeignKey(Conteudo, on_delete=models.CASCADE, related_name='episodios')
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    numero = models.IntegerField()
    temporada = models.IntegerField(default=1)
    thumbnail = models.ImageField(upload_to='episodios/', blank=True, null=True)
    video_url = models.URLField()
    duracao = models.CharField(max_length=20, blank=True)
    data_lancamento = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['temporada', 'numero']
        verbose_name = 'Episódio'
        verbose_name_plural = 'Episódios'

    def __str__(self):
        return f"{self.titulo} (T{self.temporada}E{self.numero})" 