from django.shortcuts import render, redirect
# Import login functionality
from django.contrib.auth.views import LoginView
# Import Class Based View CRUD stuff
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Default view templates
from django.views.generic import ListView, DetailView

# For login-signup stuff
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# For login protected routes
from django.contrib.auth.decorators import login_required 
# Import the mixin for class-based view protection
from django.contrib.auth.mixins import LoginRequiredMixin

# Import HttpResponse to send placeholder responses
from django.http import HttpResponse

# Import Models
from .models import Agent, Gadget, Mission
# Import form for new skills for agent
from .forms import MissionForm#, SkillForm


def home(request):
    # Placeholder HTML response
    return render(request, 'home.html')

class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def agent_index(request):
    # Placeholder HTML response
    agents = Agent.objects.all() 
    return render(request, 'agents/agent_index.html', {'agents': agents})

@login_required
def agent_detail(request, agent_id):
    agent = Agent.objects.get(id=agent_id)
    gadgets_agent_doesnt_own = Gadget.objects.exclude(id__in = agent.gadgets.all().values_list('id')) # Fetch gadgets this agent DOESNT have
    return render(request, 'agents/agent_detail.html', {
        'agent': agent,
        'gadgets': gadgets_agent_doesnt_own,
        })
    
@login_required
def gadget_index(request):
    # Placeholder HTML response
    gadgets = Gadget.objects.all() 
    return render(request, 'gadgets/gadget_index.html', {'gadgets': gadgets})
    
@login_required
def gadget_detail(request, gadget_id):
    gadget = Gadget.objects.get(id=gadget_id)
    return render(request, 'gadgets/gadget_detail.html', {
        'gadget': gadget
        })
    
@login_required
def mission_index(request):
    missions = Mission.objects.all() 
    return render(request, 'missions/mission_index.html', {'missions': missions})
    # Placeholder HTML response
    return render(request, 'missions/mission_index.html')
    
@login_required
def mission_detail(request, mission_id):
    mission = Mission.objects.get(id=mission_id)
    # agents = Agent.objects.all() 
    unassigned_agents = Agent.objects.exclude(id__in = mission.agents.all().values_list('id')) # Fetch agents this mission DOESNT have
    return render(request, 'missions/mission_detail.html', {
        'mission': mission,
        'agents': unassigned_agents
        })
    # Placeholder HTML response
    return render(request, 'missions/mission_detail.html')
    
    
# SIGN UP FUNCTIONALITY
def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in and redirect them
            login(request, user)
            return redirect('agent-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)


""" These will automatically handle CRUD form logic! """

""" AGENT CRUD """
class AgentCreate(LoginRequiredMixin, CreateView):
    model = Agent
    fields = '__all__' # Shows form of all properties, including owned user
    # Bottom excludes user
    # fields = ['code_name', 'real_name', 'agent_type', 'experience_level', 
    #           'gender', 'age', 'height_cm', 'weight_kg',
    #           'place_of_birth', 'region', 
    #           'tagline', 'description', 'previous_agency']
    
    # This inherited method is called when a
    # valid agent form is being submitted
    def form_valid(self, form):
        # Automatically assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the agent
        # Let the CreateView do its job as usual
        return super().form_valid(form)
    
class AgentUpdate(LoginRequiredMixin, UpdateView):
    model = Agent
    fields = '__all__'
    # Can disallow updating of a field by excluding it
    # fields = ['code_name', 'real_name', 'agent_type', 'experience_level', 
    #           'gender', 'age', 'height_cm', 'weight_kg',
    #           'place_of_birth', 'region', 
    #           'tagline', 'description', 'previous_agency']

class AgentDelete(LoginRequiredMixin, DeleteView):
    model = Agent
    success_url = '/agents/'
    
""" GADGET Display """

class GadgetList(LoginRequiredMixin, ListView):
    model = Gadget

class GadgetDetail(LoginRequiredMixin, DetailView):
    model = Gadget
    
# Gadget CRUD

class GadgetCreate(LoginRequiredMixin, CreateView):
    model = Gadget
    fields = '__all__'

class GadgetUpdate(LoginRequiredMixin, UpdateView):
    model = Gadget
    fields = '__all__'

class GadgetDelete(LoginRequiredMixin, DeleteView):
    model = Gadget
    success_url = '/gadgets/'
    
# Mission Display

class MissionList(LoginRequiredMixin, ListView):
    model = Mission

class MissionDetail(LoginRequiredMixin, DetailView):
    model = Mission
    
# Mission CRUD

class MissionCreate(LoginRequiredMixin, CreateView):
    model = Mission
    # fields = '__all__'
    form_class = MissionForm

class MissionUpdate(LoginRequiredMixin, UpdateView):
    model = Mission
    # fields = '__all__'
    form_class = MissionForm

class MissionDelete(LoginRequiredMixin, DeleteView):
    model = Mission
    success_url = '/missions/'
    
    
""" Associate/Removal functions"""

# Agent-Gadget association and removal
@login_required
def associate_gadget(request, agent_id, gadget_id):
    # Note that you can pass a gadget's id instead of the whole object
    Agent.objects.get(id=agent_id).gadgets.add(gadget_id)
    return redirect('agent-detail', agent_id=agent_id)

@login_required
def remove_gadget(request, agent_id, gadget_id):
    # Look up the agent
    # Look up the gadget
    # Remove the gadget from the agent
    Agent.objects.get(id=agent_id).gadgets.remove(gadget_id)
    return redirect('agent-detail', agent_id=agent_id)

# Mission-Agent association and removal
@login_required
def associate_agent(request, mission_id, agent_id):
    # Note that you can pass a gadget's id instead of the whole object
    Mission.objects.get(id=mission_id).agents.add(agent_id)
    return redirect('mission-detail', mission_id=mission_id)

@login_required
def remove_agent(request, mission_id, agent_id):
    # Look up the mission
    # Look up the agent
    # Remove the agent from the mission
    Mission.objects.get(id=mission_id).agents.remove(agent_id)
    return redirect('mission-detail', mission_id=mission_id)

# Agent-Mission association and removal
# @login_required
# def associate_mission(request, agent_id, mission_id):
#     # Note that you can pass a mission's id instead of the whole object
#     Agent.objects.get(id=agent_id).missions.add(mission_id)
#     return redirect('agent-detail', agent_id=agent_id)

# @login_required
# def remove_mission(request, agent_id, mission_id):
#     # Look up the agent
#     # Look up the mission
#     # Remove the mission from the agent
#     Agent.objects.get(id=agent_id).missions.remove(mission_id)
#     return redirect('agent-detail', agent_id=agent_id)