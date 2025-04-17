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

from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root, name='api_root'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('teams/', views.TeamList.as_view(), name='team-list'),
    path('activity/', views.ActivityList.as_view(), name='activity-list'),
    path('leaderboard/', views.LeaderboardList.as_view(), name='leaderboard-list'),
    path('workouts/', views.WorkoutList.as_view(), name='workout-list'),
]
