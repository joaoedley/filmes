# Aplicativo de Séries e Filmes

Um aplicativo mobile completo para streaming de filmes e séries com back-end Django e front-end React Native.

## 🚀 Características

- **Back-end**: Django + Django REST Framework
- **Front-end**: React Native (Android e iOS)
- **Banco de dados**: SQLite
- **Streaming**: Bunny.net
- **Anúncios**: Google AdMob
- **Sem autenticação**: Acesso livre ao conteúdo

## 📱 Funcionalidades

### Back-end (Django)
- API REST completa
- Sistema de administração
- Upload de thumbnails
- Gerenciamento de categorias
- Integração com Bunny.net

### Front-end (React Native)
- Lista de filmes/séries por categorias
- Player de vídeo integrado
- Anúncios AdMob
- Design responsivo e otimizado

## 🛠️ Instalação e Configuração

### Back-end

1. **Instalar dependências**:
```bash
pip install -r requirements.txt
```

2. **Executar migrações**:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. **Criar superusuário**:
```bash
python manage.py createsuperuser
```

4. **Executar servidor**:
```bash
python manage.py runserver
```

### Front-end

1. **Instalar dependências**:
```bash
cd mobile-app
npm install
```

2. **Executar aplicativo**:
```bash
# Android
npx react-native run-android

# iOS
npx react-native run-ios
```

## 📊 APIs Disponíveis

### Categorias
- `GET /api/categorias/` - Lista todas as categorias
- `GET /api/categorias/{id}/` - Detalhes de uma categoria
- `GET /api/categorias/{id}/conteudos/` - Conteúdos de uma categoria

### Conteúdos
- `GET /api/conteudos/` - Lista todos os conteúdos
- `GET /api/conteudos/{id}/` - Detalhes de um conteúdo
- `GET /api/conteudos/destaques/` - Conteúdos em destaque
- `GET /api/conteudos/recentes/` - Conteúdos mais recentes
- `GET /api/conteudos/por_tipo/?tipo=filme` - Filtrar por tipo

## 🎬 Estrutura do Projeto

```
filme/
├── filmeapp/           # Projeto Django principal
├── filmes/            # App Django para filmes/séries
├── media/             # Arquivos de mídia
├── mobile-app/        # Aplicativo React Native
├── requirements.txt   # Dependências Python
└── README.md         # Documentação
```

## 🔧 Configurações

### Bunny.net
Configure as URLs dos vídeos no admin Django:
1. Acesse `/admin/`
2. Vá em "Conteúdos"
3. Adicione a URL do vídeo no campo "Video URL"

### AdMob
Configure os IDs dos anúncios no arquivo de configuração do React Native.

## 📝 Licença

Este projeto é de código aberto e está disponível sob a licença MIT. 