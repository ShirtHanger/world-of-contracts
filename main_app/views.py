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
    return render(request, 'agents/agent_detail.html', {
        'agent': agent
        })

    
@login_required
def gadget_index(request):
    # Placeholder HTML response
    return render(request, 'gadgets/gadget_index.html')
    
@login_required
def gadget_detail(request):
    # Placeholder HTML response
    return render(request, 'gadgets/gadget_detail.html')
    
@login_required
def mission_index(request):
    # Placeholder HTML response
    return render(request, 'missions/mission_index.html')
    
@login_required
def mission_detail(request):
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
class AgentCreate(LoginRequiredMixin, CreateView):
    model = Agent
    fields = '__all__' # Shows form of all properties, including owned user
    # Bottom excludes user
    # fields = ['code_name', 'real_name', 'agent_type', 'experience_level', 
    #           'gender', 'age', 'height_cm', 'weight_kg'
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
    #           'gender', 'age', 'height_cm', 'weight_kg'
    #           'place_of_birth', 'region', 
    #           'tagline', 'description', 'previous_agency']

class AgentDelete(LoginRequiredMixin, DeleteView):
    model = Agent
    success_url = '/agents/'