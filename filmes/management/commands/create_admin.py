from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Cria um superusuário admin padrão'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@email.com', 'senha123')
            self.stdout.write(self.style.SUCCESS('Superusuário criado!'))
        else:
            self.stdout.write(self.style.WARNING('Superusuário já existe.')) 