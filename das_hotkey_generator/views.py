from django.shortcuts import render
from django.views import View

from .forms import DasHotkeyGeneratorForm
from .hotkey_generator import generate_hotkeys


class IndexView(View):
    form = DasHotkeyGeneratorForm
    template_name = 'das_hotkey_generator/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            hotkeys = generate_hotkeys(
                risk=cd['risk'],
                route=cd['route'],
                sc_long_key=cd['long_key'],
                sc_short_key=cd['short_key'],
                default_hotkeys=cd['default_hotkeys'])
        return render(request, self.template_name,
                      {'form': form, 'hotkeys': hotkeys})
