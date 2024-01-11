from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import livestream_signs.routing  # Import your routing configuration

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            livestream_signs.routing.websocket_urlpatterns
        )
    ),
})