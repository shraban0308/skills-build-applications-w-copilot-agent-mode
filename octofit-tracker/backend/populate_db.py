import os
import django
import random

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User, FitnessActivity

# Generate test data
def populate_test_data():
    print("Populating test data...")

    # Create test users
    for i in range(10):
        user = User.objects.create_user(
            username=f"testuser{i}",
            email=f"testuser{i}@example.com",
            password="password123"
        )
        print(f"Created user: {user.username}")

        # Create fitness activities for each user
        for j in range(5):
            activity = FitnessActivity.objects.create(
                user=user,
                activity_type=random.choice(['Running', 'Cycling', 'Swimming']),
                duration=random.randint(30, 120),  # Duration in minutes
                calories_burned=random.randint(200, 800)
            )
            print(f"Created activity for {user.username}: {activity.activity_type}")

    print("Test data population complete.")

if __name__ == "__main__":
    populate_test_data()
