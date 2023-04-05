from django.urls import path
from .views import Dashboard_information


urlpatterns = [
    path('Dashboard_information/<str:team_id>/', Dashboard_information, name='Dashboard_information'),


]