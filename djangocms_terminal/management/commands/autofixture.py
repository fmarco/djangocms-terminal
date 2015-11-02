import django
from django.core.management.base import BaseCommand, CommandError
from djangocms_terminal.utils import get_autofixture
from optparse import make_option

ARGS = (
    ('--app_label', {'dest': 'app_label', 'help': 'App label'}),
    ('--model_name', {'dest': 'model_name', 'help': 'Model name'}),
    ('--f_key', {'dest': 'f_key', 'help': 'f_key attribute for Autofixture'}),
    ('--n_instances', {'dest': 'n_instances', 'help': 'Number of instances to create'}),
)

class Command(BaseCommand):
    help = 'Generate n instance(s) of a model given a model name, the f_key parameter for Autofixture and the number of instances'

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
        if 'f_key' not in options or not options['f_key']:
            raise CommandError("f_key option required")
        # if 'n_instances' not in options or not options['n_instances']:
        #     raise CommandError("n_instances option required")
        res = get_autofixture(options['app_label'], options['model_name'], options['f_key'], int(options['n_instances']))
        self.stdout.write(res)