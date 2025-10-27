"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

import os
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

def get_api_base_url(request):
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        return f'https://{codespace_name}-8000.app.github.dev/api/'
    # fallback to request host
    return request.build_absolute_uri('/api/')

@api_view(['GET'])
def api_root(request, format=None):
    api_base = get_api_base_url(request)
    return Response({
        'users': api_base + 'users/',
        'teams': api_base + 'teams/',
        'activities': api_base + 'activities/',
        'workouts': api_base + 'workouts/',
        'leaderboard': api_base + 'leaderboard/',
    })


from . import views
router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'teams', views.TeamViewSet, basename='team')
router.register(r'activities', views.ActivityViewSet, basename='activity')
router.register(r'workouts', views.WorkoutViewSet, basename='workout')
router.register(r'leaderboard', views.LeaderboardViewSet, basename='leaderboard')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', api_root, name='api-root'),
]
