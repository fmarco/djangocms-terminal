from django.conf.urls import url

from . import views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^apps_list/$', views.installed_apps),
    url(r'^models_list/$', views.get_models),
    url(r'^model_fields/$', views.model_fields),
    url(r'^model_instance/$', views.model_instance),
    url(r'^$', TemplateView.as_view(template_name='djangocms_terminal/terminal.html'))
]