from django.test import TestCase

# Create your tests here.
from teams.models import Team


class ModelTestCase(TestCase):
    # Test if a team creation is running well
    def test_team_creation(self):
        # Create a new team
        team = Team.objects.create(name='فريقي', details="فريق الاختبار")
        # Check if team name is equal to the given name
        self.assertEqual(team.name, 'فريقي')
