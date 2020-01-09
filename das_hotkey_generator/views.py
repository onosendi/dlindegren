from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'das_hotkey_generator/index.html'
