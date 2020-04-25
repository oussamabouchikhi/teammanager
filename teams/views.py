from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView

from teams.models import Team, GameScore


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
