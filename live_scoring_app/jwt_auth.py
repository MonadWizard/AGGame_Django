from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication

User = get_user_model()

class AnonymousUser:
    def __init__(self):
        # self.is_authenticated = False
        self.is_active = False
        self.is_anonymous = True

@database_sync_to_async
def get_user(token):
    try:
        validated_token = JWTAuthentication().get_validated_token(token)
        user = JWTAuthentication().get_user(validated_token)
        print("user::::: ", user)
        return user

    except Exception:
        return AnonymousUser()



class JWTAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        headers = dict(scope["headers"])
        if b"authorization" in headers:
            # token = headers[b"authorization"].decode().split()[1]
            token = headers[b"authorization"].decode()
            scope["user"] = await get_user(token)
        else:
            scope["user"] = AnonymousUser()
        return await super().__call__(scope, receive, send)




# AnonymousUser is a class defined in django.contrib.auth.models





