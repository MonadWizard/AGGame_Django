
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    re_path(r'^aggame_images/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

installed_app_route = [    
    path("auth_user/", include("auth_user_app.urls")),
    path("dashboard/", include("dashboard_app.urls")),
    path("game/", include("game_app.urls")),
    path("home/", include("home_app.urls")),
    path("team/", include("team_app.urls")),
    path("tournament/", include("tournament_app.urls")),
]

urlpatterns = urlpatterns + installed_app_route
