# routing.py

from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('live_score/<str:userid>/<str:matchid>/', consumers.SportsScoreConsumer.as_asgi()),



]
