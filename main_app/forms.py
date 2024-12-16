from django import forms
from .models import Agent, Gadget, Mission

# All forms are imported into views.py and handle CRUD


class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        
        exclude = ['user', 'agents'] # Excludes these specific properties
        widgets = {
            'date': forms.DateInput( # Turns date into a proper date field
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }
        
class GadgetForm(forms.ModelForm):
    class Meta:
        model = Gadget
        
        exclude = ['user'] # Excludes these specific properties
        
class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        
        exclude = ['user', 'gadgets'] # Excludes these specific properties