import django
from django.core.management.base import BaseCommand, CommandError
from djangocms_terminal.utils import get_app_models
from optparse import make_option

ARGS = (
    ('--app_label', {'dest': 'app_label', 'help': 'App label'}),
)

class Command(BaseCommand):
    help = 'List of the models given an installed app'

    option_list = BaseCommand.option_list

    if django.get_version() < '1.7':
        for arg in ARGS:
            option_list = option_list + (
                make_option(
                    arg[0],
                    **arg[1]
                    ),
                )
    else:
        def add_arguments(self, parser):
            for arg in ARGS:
                parser.add_argument(arg[0], **arg[1])

    def handle(self, *args, **options):
        if 'app_label' not in options or not options['app_label']:
            raise CommandError("app_label option required")
        for model in get_app_models(options['app_label']):
            self.stdout.write(model)