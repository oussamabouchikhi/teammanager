"""teammanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from teams.views import HomePageView, TeamsListView, ScoresListView, PlayerDetailsView, TeamDetailsView, AddTeamView, \
    AddPlayerView

# Regular expression
# -     : case sensitive A != a
# \w    : alphabets, numbers & _ [A-Za-z0-9_]
# \x20  : an accept a space
# +     : compare all characters(digits)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', HomePageView.as_view(), name="home-page"),
    url(r'^teams/$', TeamsListView.as_view(), name="teams-list-view"),
    url(r'^scores/$', ScoresListView.as_view(), name="scores-list-view"),

    url(r'^player/(?P<slug>[-\w\x20]+)/$', PlayerDetailsView.as_view(), name="player-details-view"),
    url(r'^team/(?P<slug>[-\w\x20]+)/$', TeamDetailsView.as_view(), name="team-details-view"),

    url(r'^add_team/$', AddTeamView.as_view(), name="add-team-view"),
    url(r'^add_player/$', AddPlayerView.as_view(), name="add-player-view"),

]
