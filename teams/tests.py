from django.test import TestCase

# Create your tests here.
from teams.models import Team


# Test models
class ModelTestCase(TestCase):
    # Test if a team creation is running well
    def test_team_creation(self):
        # Create a new team
        team = Team.objects.create(name='فريقي', details="فريق الاختبار")
        # Check if team name is equal to the given name
        self.assertEqual(team.name, 'فريقي')


# Test Views & URLs
class ViewsTestCase(TestCase):
    def setUp(self):
        self.team1 = Team.objects.create(name='الفريق الاول', details="الفريق الاول في القائمة")
        self.team2 = Team.objects.create(name='الفريق الثاني', details="الفريق الثاني في القائمة")

    # Test if team list view is running well
    def test_teams_list_view(self):
        # Simulate a client has visited '/teams' url
        response = self.client.get('/teams/')
        # Check if response is good & teams are in context
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.team1, response.context['teams'])
        self.assertIn(self.team2, response.context['teams'])
