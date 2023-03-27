from django.urls import path
from .views import TournamentCreation , get_tournament_details


urlpatterns = [
    path("TournamentCreation/",TournamentCreation,name="TournamentCreation",),
    path("get_tournament_details/",get_tournament_details,name="get_tournament_details",),
]