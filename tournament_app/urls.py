from django.urls import path
from .views import TournamentCreation , get_tournament_details,get_tournament_info, \
        tournament_schedule, upcomming_tournament_list, tournament_update,tournament_search, \
        tournament_team_search,get_tournament_shedule, tournament_start


urlpatterns = [
    path("TournamentCreation/",TournamentCreation,name="TournamentCreation",),
    path("get_tournament_details/",get_tournament_details,name="get_tournament_details",),
    path('get_tournament_info/<str:user_id>/<int:limit>/<int:offset>/', get_tournament_info, name='get_tournament_info'),
    path('add_tournament_schedule/', tournament_schedule, name='tournament_schedule'),
    path('get_tournament_schedule/<str:tournament_id>/', get_tournament_shedule, name='get_tournament_shedule'),
    path('upcomming_tournaments/', upcomming_tournament_list, name='upcomming_tournament_list'),
    path('tournament_update/', tournament_update, name='tournament_update'),
    path('tournament_search/<str:data>/', tournament_search, name='tournament_search'),
    path('tournament_team_search/<str:data>/', tournament_team_search, name='tournament_team_search'),
    
    path('tournament_start/', tournament_start, name='tournament_start'),

]