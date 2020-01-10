from django.urls import path

from .views import IndexView

app_name = 'das_hotkey_generator'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    ]
