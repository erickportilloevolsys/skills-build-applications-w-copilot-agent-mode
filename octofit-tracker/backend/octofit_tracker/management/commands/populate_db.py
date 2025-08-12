from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Borrar datos existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Crear usuarios
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel')
        captain = User.objects.create(email='captain@marvel.com', name='Captain America', team='marvel')
        batman = User.objects.create(email='batman@dc.com', name='Batman', team='dc')
        superman = User.objects.create(email='superman@dc.com', name='Superman', team='dc')

        # Crear actividades
        Activity.objects.create(user='Iron Man', type='Running', duration=30)
        Activity.objects.create(user='Captain America', type='Cycling', duration=45)
        Activity.objects.create(user='Batman', type='Swimming', duration=60)
        Activity.objects.create(user='Superman', type='Yoga', duration=20)

        # Crear leaderboard
        Leaderboard.objects.create(team='marvel', points=75)
        Leaderboard.objects.create(team='dc', points=80)

        # Crear workouts
        Workout.objects.create(name='Morning Cardio', difficulty='Medium')
        Workout.objects.create(name='Strength Training', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
