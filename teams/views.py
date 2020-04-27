from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView

from teams.forms import TeamForm
from teams.models import Team, GameScore, Player


# Render teams using View class
class HomePageView(View):
    def get(self, request):
        # get all teams from database
        all_teams = Team.objects.all()

        # Send all teams to template as teams
        context = {
            "teams": all_teams
        }
        return render(request, 'teams_list.html', context)


# Render teams using ListView class
class TeamsListView(ListView):
    model = Team
    template_name = 'teams_list.html'
    # Send all teams to template as teams
    context_object_name = 'teams'


class ScoresListView(ListView):
    model = GameScore
    template_name = 'scores_list.html'
    context_object_name = 'scores'


class TeamDetailsView(DetailView):
    model = Team
    template_name = 'team_details.html'
    context_object_name = 'team'
    slug_field = 'name'


class PlayerDetailsView(DetailView):
    model = Player
    template_name = 'player_details.html'
    context_object_name = 'player'
    slug_field = 'name'


class AddTeamView(View):
    def get(self, request):
        form = TeamForm()
        context = {'form': form}
        return render(request, 'add_team.html', context)