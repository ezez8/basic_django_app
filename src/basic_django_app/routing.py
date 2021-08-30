import re
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import path, re_path
import jwt
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import UntypedToken
from jwt import decode as jwt_decode
from urllib.parse import parse_qs
from django.db import close_old_connections
from notifications.consumers import NotificationConsumer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AnonymousUser
from channels.middleware import BaseMiddleware
from channels.db import database_sync_to_async
from users.models import User

@database_sync_to_async
def get_user(token_key):
    # If you are using normal token based authentication
    # try:
    #     token = Token.objects.get(key=token_key)
    #     return token.user
    # except Token.DoesNotExist:
    #     return AnonymousUser()

    # If you are using jwt
    try:
        user_id: int = jwt.decode(token_key, settings.SECRET_KEY, algorithms=['HS256']).get('user_id')
    except jwt.exceptions.DecodeError:
        return AnonymousUser()
    except jwt.exceptions.ExpiredSignatureError:
        return AnonymousUser()
    try:
        return AnonymousUser() if user_id is None else User.objects.get(id=user_id)
    except User.DoesNotExist:
        return AnonymousUser()

class TokenAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        super().__init__(inner)

    async def __call__(self, scope, receive, send):
        try:
            close_old_connections()
			# Getting the token from the query string
            token_key = (dict((x.split('=') for x in scope['query_string'].decode().split("&")))).get('token', None)
			# Getting token from header
            # authorization = dict(scope['headers']).get(b'authorization', None)
            # token_key = None
            # if authorization is not None:
            #     m = re.search(r'^Bearer (?P<token>.+)$', authorization.decode())
            #     token_key = m.group('token') if m is not None else None
        except ValueError:
            token_key = None
        scope['user'] = AnonymousUser() if token_key is None else await get_user(token_key)
        return await super().__call__(scope, receive, send)

application = ProtocolTypeRouter({
	'websocket': AllowedHostsOriginValidator(
		TokenAuthMiddleware(
			URLRouter([
				path('', NotificationConsumer.as_asgi()),
			])
		)
	),
})