from django.core.management.base import BaseCommand, CommandError
from main.models import Nota
import lorem

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        for i in range(10):
            Nota.objects.create(
                titulo = lorem.sentence(),
                conteudo = lorem.paragraph()
            )
