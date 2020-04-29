from django import forms
from django.forms import ModelForm

from teams.models import Team


class TeamForm(forms.Form):
    name = forms.CharField(label='اسم الفريق')
    details = forms.CharField(label='تفاصيل الفريق')


class TeamModelForm(ModelForm):
    class Meta:
        team = Team()
        # fields = ['name', 'details']
        fields = ['__all__']
