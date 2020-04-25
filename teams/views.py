from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View

from teams.models import Team


class HomePageView(View):
    def get(self, request):
        # get all teams from database
        all_teams = Team.objects.all()

        # Send all teams to template as teams
        context = {
            "teams": all_teams
        }
        return render(request, 'teams_list.html', context)
