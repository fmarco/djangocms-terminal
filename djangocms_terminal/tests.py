# -*- coding: utf-8 -*-
from django.test import TestCase
from cms.api import create_page, add_plugin
from cms.models.placeholdermodel import Placeholder
from djangocms_terminal.cms_plugins import TerminalPlugin

class TerminalPluginTests(TestCase):

    def setUp(self):
            pass

    def test_plugin_context(self):
        placeholder = Placeholder.objects.create(slot='test')
        model_instance = add_plugin(
            placeholder,
            TerminalPlugin,
            'en',
        )
        model_instance.clean()
        plugin_instance = model_instance.get_plugin_class_instance()
        context = plugin_instance.render({}, model_instance, None)
        self.assertIn('instance', context)

    def test_plugin_html(self):
        placeholder = Placeholder.objects.create(slot='test')
        model_instance = add_plugin(
            placeholder,
            TerminalPlugin,
            'en',
        )
        model_instance.clean()
        html = model_instance.render_plugin({})
        expected_response = ('<div class="terminal_container">\n'
            '<div id="terminal"></div>\n'
            '<div id="button_terminal">TERM</div>\n</div>'
        )
        self.assertEqual(html.strip(), expected_response.strip())
