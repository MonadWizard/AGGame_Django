# routing.py

from django.urls import path
from live_scoring_app.jwt_auth import JWTAuthMiddleware
from . import consumers

websocket_urlpatterns = [
    path('live_score/<str:userid>/<str:matchid>/', consumers.SportsScoreConsumer.as_asgi()),
    path('live_score_auth/<str:matchid>/', JWTAuthMiddleware(consumers.SportsScoreConsumerAuth.as_asgi())),

    path('live_score_jwt_sync/<str:matchid>/', JWTAuthMiddleware(consumers.SportsScoreConsumersync.as_asgi())),

]
