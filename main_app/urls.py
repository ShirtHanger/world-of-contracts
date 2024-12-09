from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    
    # # Agent routes
    # path('agents/', views.agent_index, name='agents'),
    
    # # gadget routes
    # path('gadgets/', views.gadgets, name='gadgets'),
    
    # # Mission routes
    # path('missions/', views.missions, name='missions'),
    
    # Replace 'detail' with something like <int:agent_id> when database is created
    path('agents/', views.agent_index, name='agent-index'),
    path('agents/detail/', views.agent_detail, name='agent-detail'), # Agent details, collects by ID.
    
    path('gadgets/', views.gadget_index, name='gadget-index'),
    path('gadgets/detail/', views.gadget_detail, name='gadget-detail'), # Gadget details, collects by ID.
    
    path('missions/', views.mission_index, name='mission-index'),
    path('missions/detail/', views.mission_detail, name='mission-detail'), # Mission details, collects by ID.
]