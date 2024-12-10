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
    hidden_values = ('[REDACTED]', '[DATA EXPUNGED]', '[Classified]', '[Undisclosed]', '[Clearence Required]')
    expunged_data = random.choice(hidden_values)
    return expunged_data

REDACTED_LABEL = expunge_data()



# For planned 'Skill' one-to-many relationship
AGENT_SKILLS = (
    ('E', 'Espionage'),
    ('A', 'Assassination'),
    ('C', 'Counterintelligence'),
    ('I', 'Infiltration'),
    ('O', 'Covert Ops'),
    ('B', 'Black Ops'),
    ('R', 'Retaliation'),
    ('T', 'Theft'),
    ('F', 'Fieldwork'),
    ('D', 'Disguise'),
    ('H', 'Hacking')
)

# Agent limits
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
    ('T', 'Tech Specialist'),
    ('P', 'Sleeper Agent'),
)
AGENT_EXPERIENCE = (
    ('N', 'Novice'),
    ('I', 'Intermediate'),
    ('A', 'Advanced'),
    ('E', 'Expert'),
    ('M', 'Master')
)


AGENT_RACES = (
    ('R', REDACTED_LABEL), # Redacted default value
    ('W', 'White/Caucasian'),
    ('B', 'Black/African Descent'),
    ('E', 'East Asian'),
    ('S', 'South Asian/Desi'),
    ('M', 'Middle Eastern/Semitic'),
    ('L', 'Latino/Hispanic'),
    ('I', 'Indigenous/Native '),
    ('O', 'Other/Mixed'),
)

# Mission Limits
MISSION_URGENCIES = (
    ('T', 'Trivial'),
    ('L', 'Low Priority'),
    ('M', 'Medium Priority'),
    ('H', 'High Priority'),
    ('C', 'Critical'),
    ('E', 'Emergency'),
)
MISSION_TYPES = (
    ('R', 'Reconnaissance'),
    ('E', 'Extraction'),
    ('A', 'Assassination'),
    ('S', 'Sabotage'),
    ('O', 'Covert/Black Ops'),
    ('I', 'Infiltration'),
    ('D', 'Diplomatic Escort'),
    ('P', 'Protection Detail'),
    ('T', 'Training Mission'),
    ('U', 'Undercover Operation'),
)

# Gadget Limits
GADGET_TYPES = (
    ('V', 'Versatile Gadget'),
    ('T', 'Tracking'),
    ('W', 'Melee Weapon'),
    ('F', 'Firearm'),
    ('H', 'Hacking'),
    ('S', 'Surveillance'),
    ('E', 'Explosive'),
    ('L', 'Listening Bug'),
    ('D', 'Disguise Kit'),
    ('M', 'Medical Kit'),
    ('C', 'Communication'),
    ('S', 'Surveillance'),
    ('D', 'Stealth'),
    ('L', 'Lockpicking')
)



# Gadget model, many-to-many with agents. Defined above agent so code will work
class Gadget(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=250)
    
    description = models.TextField(max_length=5000)
    
    type = models.CharField(
        max_length=1, 
        choices=GADGET_TYPES,
        # Default = Flexible
        default=GADGET_TYPES[0][0]
    )
    
    manufacturer = models.CharField(max_length=100)

    def __str__(self):
        return f'({self.name} - {self.get_type_display()})'

    # Method gets the URL for a particular gadget instance
    def get_absolute_url(self):
        return reverse('gadget-detail', kwargs={'pk': self.id})


# Consider adding:
# Signature gadget (Seperate from gadgets model)
# Signature drink/clothing:
    # Agent 47's 'Black suit and tie', 
    # James Bond's' Vodka Martini, Shaken not stired'
    # Adversary (Optional, conditional render)

""" MAIN MODEL - Agents """
class Agent(models.Model):
    code_name = models.CharField(max_length=100)
    real_name = models.CharField(max_length=100, default=expunge_data())
    
    agent_type = models.CharField( # Limited choices
        max_length=1, 
        # add the 'choices' field option for the AGENT_TYPES tuple
        choices=AGENT_TYPES,
        # set the default value for meal to be Spy (S) by accessing tuple index
        default=AGENT_TYPES[0][0]
    )
    
    experience_level = models.CharField( # Limited choices
        max_length=1, 
        choices=AGENT_EXPERIENCE,
        # Default = Novice
        default=AGENT_EXPERIENCE[0][0]
    )
    
    gender = models.CharField(max_length=100, default=expunge_data())
    age = models.IntegerField(default=random.randint(20, 50))
    height_cm = models.IntegerField(default=random.randint(150, 200))
    weight_kg = models.IntegerField(default=random.randint(50, 100))
    
    place_of_birth = models.CharField(max_length=100, default=expunge_data())
    region = models.CharField(max_length=100, default=expunge_data())

    
    tagline = models.CharField(max_length=250)
    description = models.TextField(max_length=5000, default=expunge_data())
    
    previous_agency = models.CharField(max_length=100, default=expunge_data())
    
    user = models.ForeignKey(User, on_delete=models.CASCADE) # User that created agent
    
    race_or_ethnicity = models.CharField( # Limited choices
        max_length=100, 
        # add the 'choices' field option for the AGENT_RACES tuple
        choices=AGENT_RACES,
        # set the default value for meal to be [REDACTED] or something
        default=AGENT_RACES[0][0]
    )
    
    
    # missions = models.ManyToManyField(Mission) # Must define mission above agent for this to work
    
    gadgets = models.ManyToManyField(Gadget) # Must define gadget above agent for this to work
    
    # Override class object nonsense, just return the agent's code name and their type
    def __str__(self):
        return f'{self.code_name}: The {self.get_experience_level_display()} {self.get_agent_type_display()}'
    
    # Method gets the URL for a particular agent instance
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this agent's details
        return reverse('agent-detail', kwargs={'agent_id': self.id})
