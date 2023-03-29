from django.urls import path
from .views import live_score_input,start_match


urlpatterns = [
    path('live_score_input/', live_score_input, name='live_score_input'),
    path('start_match/', start_match, name='start_match'),
    

]
















