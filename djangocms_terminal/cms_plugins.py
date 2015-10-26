# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext as _


class TerminalPlugin(CMSPluginBase):
    name = _("Terminal Plugin")
    render_template = "djangocms_terminal/plugins/terminal_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(TerminalPlugin)