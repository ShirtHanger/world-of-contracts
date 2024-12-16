from django.shortcuts import render, redirect
# Class Based View CRUD stuff
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Default view templates
from django.views.generic import ListView, DetailView

# For login-signup stuff
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# For protected routes
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin

# Import HttpResponse to send placeholder responses
from django.http import HttpResponse

# Import Models
from .models import Agent, Gadget, Mission
# Form for Agent, Gadget, and Mission models
from .forms import AgentForm, GadgetForm, MissionForm

# Home pahe
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

""" AGENT SHOW PAGES """


""" Public routes """

def agent_index(request):
    agents = Agent.objects.all() 
    return render(request, 'agents/agent_index.html', {'agents': agents})

def agent_detail(request, agent_id):
    agent = Agent.objects.get(id=agent_id)
    gadgets_agent_doesnt_own = Gadget.objects.exclude(id__in = agent.gadgets.all().values_list('id')) # Fetch gadgets this agent DOESNT have
    return render(request, 'agents/agent_detail.html', {
        'agent': agent,
        'gadgets': gadgets_agent_doesnt_own,
        })
    

""" Protected routes """
@login_required
def your_agent_index(request):
    agents = Agent.objects.filter(user=request.user)
    # You could also retrieve the logged in user's agents like this
    # agents = request.user.agent_set.all()
    return render(request, 'agents/agent_index.html', { 'agents': agents })

    
""" GADGET SHOW PAGES """


""" Public routes """
def gadget_index(request):
    gadgets = Gadget.objects.all() 
    return render(request, 'gadgets/gadget_index.html', {'gadgets': gadgets})

def gadget_detail(request, gadget_id):
    gadget = Gadget.objects.get(id=gadget_id)
    return render(request, 'gadgets/gadget_detail.html', {
        'gadget': gadget
        })
""" Protected routes """

@login_required
def your_gadget_index(request):
    gadgets = Gadget.objects.filter(user=request.user)
    # You could also retrieve the logged in user's gadgets like this
    # gadgets = request.user.gadget_set.all()
    return render(request, 'gadgets/gadget_index.html', { 'gadgets': gadgets })

    

""" MISSION SHOW PAGES """


""" Public routes """
def mission_index(request):
    missions = Mission.objects.all() 
    return render(request, 'missions/mission_index.html', {'missions': missions})

def mission_detail(request, mission_id):
    mission = Mission.objects.get(id=mission_id)
    # agents = Agent.objects.all() 
    unassigned_agents = Agent.objects.exclude(id__in = mission.agents.all().values_list('id')) # Fetch agents this mission DOESNT have
    return render(request, 'missions/mission_detail.html', {
        'mission': mission,
        'agents': unassigned_agents
        })
""" Protected routes """

@login_required
def your_mission_index(request):
    missions = Mission.objects.filter(user=request.user)
    # You could also retrieve the logged in user's missions like this
    # missions = request.user.mission_set.all()
    return render(request, 'missions/mission_index.html', { 'missions': missions })
  
# SIGN UP ROUTE
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


""" 
Forms imported from forms.py. 
These will automatically handle CRUD form logic! 
"""

""" AGENT CRUD """
class AgentCreate(LoginRequiredMixin, CreateView):
    model = Agent
    form_class = AgentForm 
    
    # This inherited method is called when a
    # valid agent form is being submitted
    def form_valid(self, form):
        # Automatically assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the agent
        # Let the CreateView do its job as usual
        return super().form_valid(form)
    
class AgentUpdate(LoginRequiredMixin, UpdateView):
    model = Agent
    form_class = AgentForm

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
    form_class = GadgetForm
    def form_valid(self, form):
        # Automatically assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the gadget
        # Let the CreateView do its job as usual
        return super().form_valid(form)

class GadgetUpdate(LoginRequiredMixin, UpdateView):
    model = Gadget
    form_class = GadgetForm

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
    form_class = MissionForm
    def form_valid(self, form):
        # Automatically assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the mission
        # Let the CreateView do its job as usual
        return super().form_valid(form)

class MissionUpdate(LoginRequiredMixin, UpdateView):
    model = Mission
    form_class = MissionForm

class MissionDelete(LoginRequiredMixin, DeleteView):
    model = Mission
    success_url = '/missions/'
    
    
""" Associate/Removal functions"""

# Agent-Gadget association and removal
@login_required
def associate_gadget(request, agent_id, gadget_id):
    
    Agent.objects.get(id=agent_id).gadgets.add(gadget_id)
    return redirect('agent-detail', agent_id=agent_id)

@login_required
def remove_gadget(request, agent_id, gadget_id):
    
    Agent.objects.get(id=agent_id).gadgets.remove(gadget_id)
    return redirect('agent-detail', agent_id=agent_id)

# Mission-Agent association and removal
@login_required
def associate_agent(request, mission_id, agent_id):
    
    Mission.objects.get(id=mission_id).agents.add(agent_id)
    return redirect('mission-detail', mission_id=mission_id)

@login_required
def remove_agent(request, mission_id, agent_id):
    
    Mission.objects.get(id=mission_id).agents.remove(agent_id)
    return redirect('mission-detail', mission_id=mission_id)