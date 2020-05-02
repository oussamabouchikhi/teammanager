from django.test import TestCase

# Create your tests here.
from teams.models import Team, Player


# Test models
class ModelTestCase(TestCase):
    # Test if a team creation is running well
    def test_team_creation(self):
        # Create a new team
        team = Team.objects.create(name='فريقي', details="فريق الاختبار")
        # Check if team name is equal to the given name
        self.assertEqual(team.name, 'فريقي')

    # Todo: implement player creation test
    # Test if a team creation is running well
    # def test_player_creation(self):
    #     # Create a new player
    #     player = Player.objects.create(name='اسامة', number=10, age=21, position_in_field="مهاجم", is_captain=False)
    #     # Check if team name is equal to the given name
    #     self.assertEqual(player.name, 'اسامة')
    #     self.assertEqual(player.number, 10)
    #     self.assertEqual(player.age, 21)
    #     self.assertEqual(player.position_in_field, "مهاجم")


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
        self.assertTemplateUsed(response, 'team_list.html')
        self.assertContains(response, self.team1.name)

