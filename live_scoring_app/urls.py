from django.urls import path
from .views import input_live_Score_tournament, start_match_tournament , input_live_score_game , start_match_game, ball_type


urlpatterns = [
    path('input_live_Score_tournament/', input_live_Score_tournament, name='input_live_Score_tournament'),
    path('input_live_score_game/', input_live_score_game, name='input_live_score_game'),
    path('start_match_tournament/', start_match_tournament, name='start_match_tournament'),
    path('start_match_game/', start_match_game, name='start_match_game'),
    path('ball_type/', ball_type, name='ball_type'),

    

]
















