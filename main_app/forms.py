from django import forms
from .models import Agent, Gadget, Mission#, Skill


class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        # fields = '__all__'
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
        # fields = '__all__'
        exclude = ['user'] # Excludes these specific properties
        
class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        # fields = '__all__'
        exclude = ['user', 'gadgets'] # Excludes these specific properties