from django.urls import path

from .views import index_view

app_name = 'das_hotkey_generator'
urlpatterns = [
    path('', index_view, name='index'),
    ]
