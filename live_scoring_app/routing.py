# routing.py

from django.urls import path
<<<<<<< HEAD
=======
from live_scoring_app.jwt_auth import JWTAuthMiddleware
>>>>>>> github/production2
from . import consumers

websocket_urlpatterns = [
    path('live_score/<str:userid>/<str:matchid>/', consumers.SportsScoreConsumer.as_asgi()),
<<<<<<< HEAD
    path('live_score_auth/<str:userid>/<str:matchid>/', consumers.SportsScoreConsumerAuth.as_asgi()),



=======
    path('live_score_auth/<str:matchid>/', JWTAuthMiddleware(consumers.SportsScoreConsumerAuth.as_asgi())),

    # path('live_score_chat/', consumers.ChatConsumer.as_asgi()),

    path('live_score_jwt_auth/', JWTAuthMiddleware(consumers.YourConsumer.as_asgi())),
>>>>>>> github/production2

]
