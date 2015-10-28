import django
from django.core.management.base import BaseCommand, CommandError
from djangocms_terminal.utils import get_autofixture
from optparse import make_option

ARGS = (
    ('--model_name', {'dest': 'model_name', 'help': 'Model name'}),
    ('--f_key', {'dest': 'f_key', 'help': 'f_key attribute for Autofixture'}),
    ('--n_instances', {'dest': 'n_instances', 'help': 'Number of instances to create'}),
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
        if 'f_key' not in options or not options['f_key']:
            raise CommandError("f_key option required")
        if 'n_instances' not in options or not options['n_instances']:
            raise CommandError("n_instances option required")
        res = get_autofixture(options['model_name'], options['f_key'], options['n_instances'])
        self.stdout.write(res)