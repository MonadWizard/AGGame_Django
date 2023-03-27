from django.urls import path
from .views import team_shedule,get_team_basic_data,\
    get_team_stats,team_player_list,get_team_stats,upsert_team, \
    update_player_info_in_team,team_player_list


urlpatterns = [
    path('team_schedule/', team_shedule, name='team_schedule'),
    path('get_team_basic_data/', get_team_basic_data, name='get_team_basic_data'),
    path('get_team_stats/', get_team_stats, name='get_team_stats'),

    path('team_player_list/', team_player_list, name='team_player_list'),
    path('get_team_stats/', get_team_stats, name='get_team_stats'),
    path('upsert_team/', upsert_team, name='upsert_team'),
    path('update_player_info_in_team/', update_player_info_in_team, name='update_player_info_in_team'),
    path('team_player_list/', team_player_list, name='team_player_list'),

]