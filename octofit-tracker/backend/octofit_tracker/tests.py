from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Team, Activity, Leaderboard, Workout
from django.contrib.auth.models import User

class APITests(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel')
        self.user = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass')
        self.activity = Activity.objects.create(user='ironman', team='Marvel', type='Run', duration=30)
        self.leaderboard = Leaderboard.objects.create(team='Marvel', points=75)
        self.workout = Workout.objects.create(name='Pushups', difficulty='Easy')

    def test_api_root(self):
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_team_list(self):
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_activity_list(self):
        url = reverse('activity-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_leaderboard_list(self):
        url = reverse('leaderboard-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_workout_list(self):
        url = reverse('workout-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
