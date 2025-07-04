from django.core.management.base import BaseCommand
from filmes.models import Categoria, Conteudo


class Command(BaseCommand):
    help = 'Popula o banco de dados com categorias e conteúdos de exemplo'

    def handle(self, *args, **options):
        self.stdout.write('Criando categorias...')
        
        # Criar categorias
        categorias = [
            {
                'nome': 'Ação',
                'descricao': 'Filmes e séries de ação e aventura',
                'cor': '#FF6B6B',
                'ordem': 1
            },
            {
                'nome': 'Comédia',
                'descricao': 'Filmes e séries de comédia',
                'cor': '#4ECDC4',
                'ordem': 2
            },
            {
                'nome': 'Drama',
                'descricao': 'Filmes e séries dramáticos',
                'cor': '#45B7D1',
                'ordem': 3
            },
            {
                'nome': 'Terror',
                'descricao': 'Filmes e séries de terror',
                'cor': '#96CEB4',
                'ordem': 4
            },
            {
                'nome': 'Romance',
                'descricao': 'Filmes e séries românticos',
                'cor': '#FFEAA7',
                'ordem': 5
            },
            {
                'nome': 'Ficção Científica',
                'descricao': 'Filmes e séries de ficção científica',
                'cor': '#DDA0DD',
                'ordem': 6
            }
        ]
        
        for cat_data in categorias:
            categoria, created = Categoria.objects.get_or_create(
                nome=cat_data['nome'],
                defaults=cat_data
            )
            if created:
                self.stdout.write(f'Categoria criada: {categoria.nome}')
        
        self.stdout.write('Criando conteúdos de exemplo...')
        
        # Conteúdos de exemplo
        conteudos = [
            {
                'titulo': 'Vingadores: Ultimato',
                'descricao': 'Após os eventos devastadores de "Vingadores: Guerra Infinita", o universo está em ruínas. Com a ajuda dos aliados restantes, os Vingadores se reúnem mais uma vez para reverter as ações de Thanos e restaurar o equilíbrio do universo.',
                'tipo': 'filme',
                'categoria_nome': 'Ação',
                'duracao': '3h 1min',
                'ano': 2019,
                'classificacao': '12',
                'destaque': True,
                'video_url': 'https://example.bunny.net/video/vingadores-ultimato.mp4'
            },
            {
                'titulo': 'Friends',
                'descricao': 'Seis amigos que vivem no mesmo bairro em Manhattan enfrentam a vida e os amores em Nova York e se envolvem em confusões e dilemas pessoais.',
                'tipo': 'serie',
                'categoria_nome': 'Comédia',
                'duracao': '22min',
                'ano': 1994,
                'classificacao': '12',
                'destaque': True,
                'video_url': 'https://example.bunny.net/video/friends-s01e01.mp4'
            },
            {
                'titulo': 'Breaking Bad',
                'descricao': 'Um professor de química do ensino médio vira fabricante de metanfetamina, passando por uma transformação gradual de um homem comum em um temido criminoso.',
                'tipo': 'serie',
                'categoria_nome': 'Drama',
                'duracao': '47min',
                'ano': 2008,
                'classificacao': '16',
                'destaque': True,
                'video_url': 'https://example.bunny.net/video/breaking-bad-s01e01.mp4'
            },
            {
                'titulo': 'Interestelar',
                'descricao': 'Uma equipe de exploradores viaja através de um buraco de minhoca no espaço na tentativa de garantir a sobrevivência da humanidade.',
                'tipo': 'filme',
                'categoria_nome': 'Ficção Científica',
                'duracao': '2h 49min',
                'ano': 2014,
                'classificacao': '12',
                'destaque': False,
                'video_url': 'https://example.bunny.net/video/interestelar.mp4'
            },
            {
                'titulo': 'O Exorcista',
                'descricao': 'Quando uma jovem é possuída por uma entidade demoníaca, sua mãe desesperada busca a ajuda de dois padres para realizar um exorcismo.',
                'tipo': 'filme',
                'categoria_nome': 'Terror',
                'duracao': '2h 2min',
                'ano': 1973,
                'classificacao': '18',
                'destaque': False,
                'video_url': 'https://example.bunny.net/video/o-exorcista.mp4'
            },
            {
                'titulo': 'Titanic',
                'descricao': 'Um jovem artista pobre e uma jovem rica se apaixonam a bordo do navio durante sua viagem inaugural do Southampton para Nova York.',
                'tipo': 'filme',
                'categoria_nome': 'Romance',
                'duracao': '3h 14min',
                'ano': 1997,
                'classificacao': '12',
                'destaque': True,
                'video_url': 'https://example.bunny.net/video/titanic.mp4'
            }
        ]
        
        for cont_data in conteudos:
            categoria = Categoria.objects.get(nome=cont_data['categoria_nome'])
            conteudo, created = Conteudo.objects.get_or_create(
                titulo=cont_data['titulo'],
                defaults={
                    'descricao': cont_data['descricao'],
                    'tipo': cont_data['tipo'],
                    'categoria': categoria,
                    'duracao': cont_data['duracao'],
                    'ano': cont_data['ano'],
                    'classificacao': cont_data['classificacao'],
                    'destaque': cont_data['destaque'],
                    'video_url': cont_data['video_url']
                }
            )
            if created:
                self.stdout.write(f'Conteúdo criado: {conteudo.titulo}')
        
        self.stdout.write(
            self.style.SUCCESS('Dados populados com sucesso!')
        ) 