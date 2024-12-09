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
from .models import Agent#, Gadget, Mission
# Import form for new skills for agent
#from .forms import SkillForm


def home(request):
    # Placeholder HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def agent_index(request):
    # Placeholder HTML response
    agents = Agent.objects.all() 
    return render(request, 'agents/agent_index.html', {'agents': agents})
    

def agent_detail(request):
    # Placeholder HTML response
    return render(request, 'agents/agent_detail.html')

    

def gadget_index(request):
    # Placeholder HTML response
    return render(request, 'gadgets/gadget_index.html')
    

def gadget_detail(request):
    # Placeholder HTML response
    return render(request, 'gadgets/gadget_detail.html')
    

def mission_index(request):
    # Placeholder HTML response
    return render(request, 'missions/mission_index.html')
    

def mission_detail(request):
    # Placeholder HTML response
    return render(request, 'missions/mission_detail.html')
    