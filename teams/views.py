from django.db import IntegrityError
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView

from teams.forms import TeamForm, TeamModelForm, ScoreModelForm, PlayerModelForm
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
        return render(request, 'home.html', context)


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

    def get_context_data(self, **kwargs):
        context = super(ScoresListView, self).get_context_data(**kwargs)
        context['form'] = ScoreModelForm()
        return context

    # Create a new game-score from form
    def post(self, request, *args, **kwargs):
        form = ScoreModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/scores/')


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
        form = TeamModelForm()
        context = {'form': form}
        return render(request, 'add_team.html', context)

    def post(self, request):
        form = TeamModelForm(request.POST)
        # if form data are valid
        if form.is_valid():
            form.save()  # save data
            return redirect('/')  # redirect to home after saving
        # if form data are not valid
        else:
            context = {'form': form}
            return render(request, 'add_team.html', context)


class AddPlayerView(View):
    def get(self, request):
        form = PlayerModelForm()
        context = {'form': form}
        return render(request, 'add_player.html', context)

    def post(self, request):
        form = PlayerModelForm(request.POST)
        # if form data are valid
        if form.is_valid():
            form.save()  # save data
            return redirect('/')  # redirect to home after saving
        # if form data are not valid
        else:
            context = {'form': form}
            return render(request, 'add_player.html', context)
