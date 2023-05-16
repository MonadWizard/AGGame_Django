from django.urls import path
from .views import Dashboard_information, dash_game, dash_tournament


urlpatterns = [
    path('Dashboard_information/<str:team_id>/', Dashboard_information, name='Dashboard_information'),
    path('dash_game/<str:team_id>/', dash_game, name='dash_game'),
    path('dash_tournament/<str:team_id>/', dash_tournament, name='dash_tournament'),



]