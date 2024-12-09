# main_app/views.py

from django.shortcuts import render

# Import HttpResponse to send text-based responses
from django.http import HttpResponse


def home(request):
    # Placeholder HTML response
    return render(request, 'home.html')
    return HttpResponse('<h1>[DATA EXPUNGED] [Render this properly]</h1>')

def about(request):
    return render(request, 'about.html')

def agent_index(request):
    # Placeholder HTML response
    return render(request, 'agents/agent_index.html')
    return HttpResponse('<h1>Your created agents: [DATA EXPUNGED] [Render this properly]</h1>')

def agent_detail(request):
    # Placeholder HTML response
    return render(request, 'agents/agent_detail.html')
    return HttpResponse('<h1>Your created agents: [DATA EXPUNGED] [Render this properly]</h1>')

def gadget_index(request):
    # Placeholder HTML response
    return render(request, 'gadgets/gadget_index.html')
    return HttpResponse('<h1>Your created gadgets: [DATA EXPUNGED] [Render this properly]</h1>')

def gadget_detail(request):
    # Placeholder HTML response
    return render(request, 'gadgets/gadget_detail.html')
    return HttpResponse('<h1>Your created gadgets: [DATA EXPUNGED] [Render this properly]</h1>')

def mission_index(request):
    # Placeholder HTML response
    return render(request, 'missions/mission_index.html')
    return HttpResponse('<h1>Missions: [DATA EXPUNGED] [Render this properly]</h1>')

def mission_detail(request):
    # Placeholder HTML response
    return render(request, 'missions/mission_detail.html')
    return HttpResponse('<h1>Missions: [DATA EXPUNGED] [Render this properly]</h1>')