from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    path('machine/', consumers.PNPConsumer.as_asgi()),
]
