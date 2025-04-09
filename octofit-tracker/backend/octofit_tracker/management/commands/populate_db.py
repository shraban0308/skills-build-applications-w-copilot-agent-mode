from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            User(_id=ObjectId(), username='superman', email='superman@merington.edu', password='supermanpassword'),
            User(_id=ObjectId(), username='wonderwoman', email='wonderwoman@merington.edu', password='wonderwomanpassword'),
            User(_id=ObjectId(), username='batman', email='batman@merington.edu', password='batmanpassword'),
            User(_id=ObjectId(), username='flash', email='flash@merington.edu', password='flashpassword'),
            User(_id=ObjectId(), username='aquaman', email='aquaman@merington.edu', password='aquamanpassword'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        blue_team = Team(_id=ObjectId(), name='Blue Team')
        gold_team = Team(_id=ObjectId(), name='Gold Team')
        blue_team.save()
        gold_team.save()
        for user in users[:3]:
            blue_team.members.add(user)
        for user in users[3:]:
            gold_team.members.add(user)

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Cycling', duration=timedelta(hours=1)),
            Activity(_id=ObjectId(), user=users[1], activity_type='Crossfit', duration=timedelta(hours=2)),
            Activity(_id=ObjectId(), user=users[2], activity_type='Running', duration=timedelta(hours=1, minutes=30)),
            Activity(_id=ObjectId(), user=users[3], activity_type='Strength', duration=timedelta(minutes=30)),
            Activity(_id=ObjectId(), user=users[4], activity_type='Swimming', duration=timedelta(hours=1, minutes=15)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), user=users[0], score=120),
            Leaderboard(_id=ObjectId(), user=users[1], score=110),
            Leaderboard(_id=ObjectId(), user=users[2], score=105),
            Leaderboard(_id=ObjectId(), user=users[3], score=95),
            Leaderboard(_id=ObjectId(), user=users[4], score=85),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', duration=timedelta(hours=1)),
            Workout(_id=ObjectId(), name='Crossfit', duration=timedelta(hours=2)),
            Workout(_id=ObjectId(), name='Running Training', duration=timedelta(hours=1, minutes=30)),
            Workout(_id=ObjectId(), name='Strength Training', duration=timedelta(minutes=30)),
            Workout(_id=ObjectId(), name='Swimming Training', duration=timedelta(hours=1, minutes=15)),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the OctoFit database with test data.'))