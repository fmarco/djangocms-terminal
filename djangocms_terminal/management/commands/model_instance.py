import django
from django.core.management.base import BaseCommand, CommandError
from djangocms_terminal.utils import get_model_instance
from optparse import make_option

ARGS = (
    ('--app_label', {'dest': 'app_label', 'help': 'App label'}),
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
        if 'app_label' not in options or not options['app_label']:
            raise CommandError("app_label option required")
        if 'model_name' not in options or not options['model_name']:
            raise CommandError("model_name option required")
        extras = {}
        if 'attrs' in options and options['attrs']:
            extras['args'] = options['attrs']
        print options
        res = get_model_instance(options['app_label'], options['model_name'], **extras)
        self.stdout.write(res)