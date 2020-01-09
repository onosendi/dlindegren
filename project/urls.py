from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('default.urls')),
    path('misc/das-hotkey-generator', include('das_hotkey_generator.urls')),
]
