from django.urls import path
from .views import MatchCreation,get_team_by_specific_creator,\
    get_all_team_list_by_game_name,team_and_player_info,upcomming_game_list


urlpatterns = [
    path("MatchCreation/",MatchCreation,name="MatchCreation"),
    path("get_team_by_specific_creator/",get_team_by_specific_creator,name="get_team_by_specific_creator"),
    path("get_all_team_list_by_game_name/",get_all_team_list_by_game_name,name="get_all_team_list_by_game_name"),
    path("team_and_player_info/",team_and_player_info,name="team_and_player_info"),

    path("upcomming_game_list/",upcomming_game_list,name="upcomming_game_list"),

]