import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'w2wproject.settings')

application = get_asgi_application()


from chat import routing
from chat.token_middleware import TokenMiddleware


application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': TokenMiddleware(
        URLRouter(
            routing.websocket_urlpatterns)
    )
})
