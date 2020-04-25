from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View

from teams.models import Team


class HomePageView(View):
    def get(self, request):
        # get all teams from database
        teams = Team.objects.all()
        return HttpResponse(teams)