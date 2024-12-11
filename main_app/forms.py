from django import forms
from .models import Mission#, Skill


class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = '__all__' # meals is limited ot breakfast, lunch, dinner as it was on models.py
        widgets = {
            'date': forms.DateInput( # Turns date into a proper date field
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }