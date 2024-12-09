from django.db import models # Imports models class so you can create API classes
from django.urls import reverse 
from datetime import date
import random #I think this will let me randomize defaults

# Create your models here.

# Import the default User model
from django.contrib.auth.models import User

from django.db import models

# hidden_values = ('[REDACTED]', '[DATA EXPUNGED], [Classified]')
# default='[REDACTED]'
# default=random.choice(hidden_values)

# Unrequired values will be [REDACTED] if not provided
def expunge_data():
    hidden_values = ('[REDACTED]', '[DATA EXPUNGED], [Classified]')
    expunged_data = random.choice(hidden_values)
    return expunged_data



# For planned 'Skill' one-to-many relationship
AGENT_SKILLS = (
    ('E', 'Espionage'),
    ('A', 'Assassination'),
    ('C', 'Counterintelligence'),
    ('I', 'Infiltration'),
    ('O', 'Covert Operations'),
    ('R', 'Retaliation'),
    ('T', 'Theft'),
    ('F', 'Fieldwork'),
    ('D', 'Disguise'),
    ('H', 'Hacking')
)


AGENT_TYPES = (
    ('S', 'Spy'),
    ('A', 'Assassin'),
    ('C', 'Covert Operative'),
    ('E', 'Enforcer'),
    ('U', 'Undercover Agent'),
    ('R', 'Recruiter'),
    ('H', 'Handler'),
    ('L', 'Logistics Specialist'),
    ('W', 'Weapons Specialist'),
    ('T', 'Tech Specialist')
)


AGENT_EXPERIENCE = (
    ('N', 'Novice'),
    ('I', 'Intermediate'),
    ('A', 'Advanced'),
    ('E', 'Expert'),
    ('M', 'Master')
)


class Agent(models.Model):
    code_name = models.CharField(max_length=100)
    real_name = models.CharField(max_length=100, default=expunge_data())
    
    agent_type = models.CharField( # Limited choices
        max_length=100, 
        # add the 'choices' field option for the AGENT_TYPES tuple
        choices=AGENT_TYPES,
        # set the default value for meal to be Spy (S) by accessing tuple index
        default=AGENT_TYPES[0]
    )
    
    experience_level = models.CharField( # Limited choices
        max_length=100, 
        choices=AGENT_EXPERIENCE,
        # Default = Novice
        default=AGENT_EXPERIENCE[0]
    )
    
    gender = models.CharField(max_length=100, default='Unknown')
    age = models.IntegerField(default=random.randint(20, 50))
    height_cm = models.IntegerField(default=random.randint(150, 200))
    weight_kg = models.IntegerField(default=random.randint(50, 100))
    
    place_of_birth = models.CharField(max_length=100, default=expunge_data())
    region = models.CharField(max_length=100, default=expunge_data())
    
    tagline = models.TextField(max_length=250)
    description = models.TextField(max_length=1000, default=expunge_data())
    
    previous_agency = models.CharField(max_length=100, default=expunge_data())
    
    # user = models.ForeignKey(User, on_delete=models.CASCADE) # User
    
    # missions = models.ManyToManyField(Mission) # Must define mission above agent for this to work
    
    # gadgets = models.ManyToManyField(Gadget) # Must define gadget above agent for this to work
    
    # Override class object nonsense, just return the agent's code name and their type
    def __str__(self):
        return f'{self.code_name} - the {self.experience_level} {self.agent_type}'
    
    # Method gets the URL for a particular agent instance
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this agent's details
        return reverse('agent-detail', kwargs={'agent_id': self.id})
