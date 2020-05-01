from django import forms
from django.forms import ModelForm
from crispy_forms import layout
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from teams.models import Team, GameScore, Player


class TeamForm(forms.Form):
    name = forms.CharField(label='اسم الفريق')
    details = forms.CharField(label='تفاصيل الفريق')


class PlayerForm(forms.Form):
    name = forms.CharField(label='اسم اللاعب')
    number = forms.IntegerField(label='رقم اللاعب')
    age = forms.IntegerField(label='عمر اللاعب')
    position_in_field = forms.CharField(label='الموقع في الملعب')
    is_captain = forms.BooleanField(label='هل هو قائد الفريق')
    team = forms.CharField(label='اسم الفريق')


class TeamModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TeamModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'اضافة'))

    class Meta:
        model = Team
        # fields = ['name', 'details']
        fields = '__all__'
        labels = {
            'name': 'اسم الفريق',
            'details': 'تفاصيل الفريق',
        }

        error_messages = {
            'name': {
                'unique': 'عذرا هذا الاسم مكرر, يرجى تغيير الاسم',
            }
        }


class PlayerModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PlayerModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'اضافة'))

    class Meta:
        model = Player

        fields = '__all__'
        labels = {
            'name': 'اسم اللاعب',
            'number': 'رقم اللاعب',
            'age': 'عمر اللاعب',
            'position_in_field': 'الموقع في الملعب',
            'is_captain': 'هل هو قائد الفريق',
            'team': 'فريق اللاعب',
        }

        error_messages = {
            'number': {
                'unique': 'عذرا هذا الرقم مأخود, يرجى اختيار رقم اخر',
            }
        }


class ScoreModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ScoreModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'اضافة'))

    class Meta:
        model = GameScore
        exclude = ['game_date']  # get all fields except game_date

        labels = {
            'first_team_relation': 'اسم الفريق الاول',
            'second_team_relation': 'اسم الفريق الثاني',
            'first_team_score': 'نتيجة الفريق الاول',
            'second_team_score': 'نتيجة الفريق الثاني',
        }
