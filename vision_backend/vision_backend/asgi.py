"""
ASGI config for vision_backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import api.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vision_backend.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        api.routing.websocket_urlpatterns  # <-- attach WebSocket routes here
    ),
})
