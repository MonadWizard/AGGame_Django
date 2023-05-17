import os
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from live_scoring_app import routing
<<<<<<< HEAD

=======
from live_scoring_app.jwt_auth import JWTAuthMiddleware
>>>>>>> github/production2

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aggame_project.settings')


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns)),
    }
)

