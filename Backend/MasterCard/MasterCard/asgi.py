import os
import django
from django.core.asgi import get_asgi_application

# Set the default settings module for the 'django' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MasterCard.settings')

# Setup Django
django.setup()

# Import Channels-related modules
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from MasterCard.routing import websocket_urlpatterns  # Import your WebSocket URL patterns
from userManagement.middleware import JWTAuthMiddleware  # Adjust if needed

# Create the ASGI application
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Handles HTTP requests
    "websocket": JWTAuthMiddleware(  # Handles WebSocket requests with JWT middleware
        URLRouter(
            websocket_urlpatterns  # List of WebSocket URL patterns from CardScanning
        )
    ),
})
