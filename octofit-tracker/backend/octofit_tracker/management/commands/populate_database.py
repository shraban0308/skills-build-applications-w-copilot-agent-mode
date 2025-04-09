import os
import django
from django.core.management.base import BaseCommand
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        print('Populating database with test data...')

        # Populate users
        for user_data in test_users:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={
                    'email': user_data['email'],
                    'password': user_data['password']
                }
            )
            if created:
                print(f'Created user: {user.username}')

        # Populate teams
        for team_data in test_teams:
            team, created = Team.objects.get_or_create(name=team_data['name'])
            if created:
                for member_username in team_data['members']:
                    user = User.objects.get(username=member_username)
                    team.members.add(user)
                print(f'Created team: {team.name}')

        # Populate activities
        for activity_data in test_activities:
            user = User.objects.get(username=activity_data['username'])
            activity, created = Activity.objects.get_or_create(
                user=user,
                activity_type=activity_data['activity_type'],
                duration=activity_data['duration'],
                calories_burned=activity_data['calories_burned']
            )
            if created:
                print(f'Created activity for {user.username}: {activity.activity_type}')

        # Populate leaderboard
        for leaderboard_data in test_leaderboard:
            user = User.objects.get(username=leaderboard_data['username'])
            leaderboard, created = Leaderboard.objects.get_or_create(
                user=user,
                score=leaderboard_data['score']
            )
            if created:
                print(f'Added {user.username} to leaderboard with {leaderboard.score} points')

        # Populate workouts
        for workout_data in test_workouts:
            workout, created = Workout.objects.get_or_create(
                name=workout_data['name'],
                description=workout_data['description']
            )
            if created:
                print(f'Created workout: {workout.name}')

        print('Database population complete.')

print("populate_database.py loaded successfully")
print("Command class:", Command)