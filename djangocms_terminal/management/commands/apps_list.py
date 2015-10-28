from django.core.management.base import BaseCommand, CommandError
from djangocms_terminal.utils import get_installed_apps

class Command(BaseCommand):
    help = 'List of the installed apps'

    def handle(self, *args, **options):
        for app in get_installed_apps():
            self.stdout.write(app)