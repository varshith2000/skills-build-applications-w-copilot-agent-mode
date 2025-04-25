from django.http import JsonResponse
from rest_framework import viewsets
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request):
    base_url = 'https://symmetrical-guide-65v9g9p75pg2qxx-8000.app.github.dev/'
    return Response({
        'users': base_url + 'users/',
        'teams': base_url + 'teams/',
        'activities': base_url + 'activity/',
        'leaderboard': base_url + 'leaderboard/',
        'workouts': base_url + 'workouts/'
    })

class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamList(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityList(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardList(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutList(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

def users_simple_api(request):
    data = list(User.objects.values())
    return JsonResponse(data, safe=False)