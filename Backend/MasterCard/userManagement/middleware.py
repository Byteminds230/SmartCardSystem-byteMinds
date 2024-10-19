import jwt
from channels.middleware import BaseMiddleware
from django.contrib.auth.models import AnonymousUser
from django.conf import settings
from urllib.parse import parse_qs
from .models import *
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from asgiref.sync import sync_to_async
class JWTAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        # Extract token from the query string (for WebSocket)
        query_string = parse_qs(scope["query_string"].decode())
        token = query_string.get("token")

        if token:
            try:
                # Validate the JWT token
                access_token = AccessToken(token[0])
                user_id = access_token.get("user_id")
                scope["user"] = await sync_to_async(CustomUser.objects.get)(id=user_id)
            except (InvalidToken, CustomUser.DoesNotExist, TokenError):
                scope["user"] = AnonymousUser()
        else:
            scope["user"] = AnonymousUser()

        return await super().__call__(scope, receive, send)