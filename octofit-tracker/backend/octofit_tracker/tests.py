from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(email='test@hero.com', name='Test Hero', team='marvel')
    def test_user_email(self):
        user = User.objects.get(name='Test Hero')
        self.assertEqual(user.email, 'test@hero.com')

class TeamTestCase(TestCase):
    def setUp(self):
        Team.objects.create(name='marvel')
    def test_team_name(self):
        team = Team.objects.get(name='marvel')
        self.assertEqual(team.name, 'marvel')
