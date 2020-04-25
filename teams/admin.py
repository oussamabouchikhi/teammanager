from django.contrib import admin

# Register your models here.
# to display tables in '/admin' we need to register models here
from teams.models import Team, Player, GameScore

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(GameScore)