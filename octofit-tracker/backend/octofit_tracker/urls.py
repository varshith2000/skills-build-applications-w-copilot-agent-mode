"""
URL configuration for octofit_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserList)
router.register(r'teams', views.TeamList)
router.register(r'activity', views.ActivityList)
router.register(r'leaderboard', views.LeaderboardList)
router.register(r'workouts', views.WorkoutList)

urlpatterns = [
    path('', views.api_root, name='api_root'),
    path('', include(router.urls)),
    path('users-simple/', views.users_simple_api, name='users_simple_api'),
]
