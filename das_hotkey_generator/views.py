from django.shortcuts import render

from .forms import DasHotkeyGeneratorForm
from .hotkey_generator import generate_hotkeys


def index_view(request):
    hotkeys = None
    form = DasHotkeyGeneratorForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        hotkeys = generate_hotkeys(
            risk=cd['risk'],
            route=cd['route'],
            sc_long_key=cd['long_key'],
            sc_short_key=cd['short_key'],
            default_hotkeys=cd['default_hotkeys'])
    return render(request, 'das_hotkey_generator/index.html',
                  {'form': form,
                   'hotkeys': hotkeys})
