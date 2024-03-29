# your_project_name/routing.py
from django.urls import re_path
from livestream_signs.consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_id>\d+)/$', ChatConsumer.as_asgi()),
]
