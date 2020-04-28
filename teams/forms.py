from django import forms


class TeamForm(forms.Form):
    name = forms.CharField(label='اسم الفريق')
    details = forms.CharField(label='تفاصيل الفريق')