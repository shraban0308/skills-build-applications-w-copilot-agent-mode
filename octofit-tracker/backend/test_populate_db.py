import os
import django
from octofit_tracker.management.commands.populate_database import Command

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

if __name__ == "__main__":
    command = Command()
    command.handle()
