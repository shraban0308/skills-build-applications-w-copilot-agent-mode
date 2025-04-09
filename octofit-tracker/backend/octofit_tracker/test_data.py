from datetime import timedelta

# Test data for OctoFit Tracker

test_users = [
    {"username": "student1", "email": "student1@example.com", "password": "password123"},
    {"username": "student2", "email": "student2@example.com", "password": "password123"},
    {"username": "student3", "email": "student3@example.com", "password": "password123"},
]

test_teams = [
    {"name": "Team Alpha", "members": ["student1", "student2"]},
    {"name": "Team Beta", "members": ["student3"]},
]

test_activities = [
    {"username": "student1", "activity_type": "Running", "duration": timedelta(minutes=30), "calories_burned": 300},
    {"username": "student2", "activity_type": "Cycling", "duration": timedelta(minutes=45), "calories_burned": 400},
    {"username": "student3", "activity_type": "Swimming", "duration": timedelta(minutes=60), "calories_burned": 500},
]

test_leaderboard = [
    {"username": "student1", "score": 100},
    {"username": "student2", "score": 80},
    {"username": "student3", "score": 120},
]

test_workouts = [
    {"name": "Morning Run", "description": "A quick 5km run to start the day."},
    {"name": "Evening Yoga", "description": "Relaxing yoga session to wind down."},
]
