from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="hyungi").exists():
            User.objects.create_superuser("hyungi", "hyeonik7@gmail.com", "hyungi")
            self.stdout.write(self.style.SUCCESS('Successfully created new super user'))
