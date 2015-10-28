import django
from django.core.management.base import BaseCommand, CommandError
from djangocms_terminal.utils import get_model_instance
from optparse import make_option

ARGS = (
    ('--model_name', {'dest': 'model_name', 'help': 'Model name'}),
    ('--attrs', {'dest': 'attrs', 'help': 'Attribute key/value list'}),
)

class Command(BaseCommand):
    help = 'Create an instance of a model given a model name'

    option_list = BaseCommand.option_list

    if django.get_version() < '1.8':
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
        if 'model_name' not in options or not options['model_name']:
            raise CommandError("model_name option required")
        if 'attrs' not in options or not options['attrs']:
            raise CommandError("attrs option required")
        res = get_model_instance(options['model_name'], options['attrs'])
        self.stdout.write(res)