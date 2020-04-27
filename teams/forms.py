from django import forms


class TeamForm(forms.Form):
    name = forms.CharField()
    details = forms.CharField()