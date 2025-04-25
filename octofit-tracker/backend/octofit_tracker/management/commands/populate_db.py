from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor'),
            User(email='metalgeek@mhigh.edu', name='Tony Stark'),
            User(email='zerocool@mhigh.edu', name='Elliot Alderson'),
            User(email='crashoverride@mhigh.edu', name='Dade Murphy'),
            User(email='sleeptoken@mhigh.edu', name='Sleep Token'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team_blue = Team(name='Blue Team', members=[user.email for user in users[:3]])
        team_gold = Team(name='Gold Team', members=[user.email for user in users[3:]])
        team_blue.save()
        team_gold.save()

        # Create activities
        activities = [
            Activity(user_email='thundergod@mhigh.edu', activity_type='Cycling', duration=60),
            Activity(user_email='metalgeek@mhigh.edu', activity_type='Crossfit', duration=120),
            Activity(user_email='zerocool@mhigh.edu', activity_type='Running', duration=90),
            Activity(user_email='crashoverride@mhigh.edu', activity_type='Strength', duration=30),
            Activity(user_email='sleeptoken@mhigh.edu', activity_type='Swimming', duration=75),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user_email='thundergod@mhigh.edu', points=100),
            Leaderboard(user_email='metalgeek@mhigh.edu', points=90),
            Leaderboard(user_email='zerocool@mhigh.edu', points=95),
            Leaderboard(user_email='crashoverride@mhigh.edu', points=85),
            Leaderboard(user_email='sleeptoken@mhigh.edu', points=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
