from django import forms

from .models import FamousPerson, User, Professions


class FamousPersonForm(forms.ModelForm):

    class Meta:
        model = FamousPerson
        fields = ('name', 'birth_date', 'profession',)

