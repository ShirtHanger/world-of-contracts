from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    
    # Replace 'detail' with something like <int:agent_id> when database is created
    
    
    # Agent routes
    path('agents/', views.agent_index, name='agent-index'),
    path('your-agents/', views.your_agent_index, name='your-agent-index'),
    path('agents/<int:agent_id>/', views.agent_detail, name='agent-detail'), # Agent details, collects by ID.
    
    path('agents/create/', views.AgentCreate.as_view(), name='agent-create'),
    path('agents/<int:pk>/update/', views.AgentUpdate.as_view(), name='agent-update'),
    path('agents/<int:pk>/delete/', views.AgentDelete.as_view(), name='agent-delete'),
    
    # Agent skills route
    # path(
    # 'agents/<int:agent_id>/add-skill/', 
    # views.add_skill, 
    # name='add-skill'
    # ),
    
    # Gadget Routes
    path('gadgets/', views.gadget_index, name='gadget-index'),
    path('your-gadgets/', views.your_gadget_index, name='your-gadget-index'),
    path('gadgets/<int:gadget_id>/', views.gadget_detail, name='gadget-detail'), # Gadget details, collects by ID.
    
    path('gadgets/create/', views.GadgetCreate.as_view(), name='gadget-create'),
    path('gadgets/<int:pk>/update/', views.GadgetUpdate.as_view(), name='gadget-update'),
    path('gadgets/<int:pk>/delete/', views.GadgetDelete.as_view(), name='gadget-delete'),
    
    # Mission Routes
    path('missions/', views.mission_index, name='mission-index'),
    path('your-missions/', views.your_mission_index, name='your-mission-index'),
    path('missions/<int:mission_id>/', views.mission_detail, name='mission-detail'), # Mission details, collects by ID.
    
    path('missions/create/', views.MissionCreate.as_view(), name='mission-create'),
    path('missions/<int:pk>/update/', views.MissionUpdate.as_view(), name='mission-update'),
    path('missions/<int:pk>/delete/', views.MissionDelete.as_view(), name='mission-delete'),
    
    # Association/Removal routes
    
    # Agent-Gadget Association/removal
    path('agents/<int:agent_id>/associate-gadget/<int:gadget_id>/', views.associate_gadget, name='associate-gadget'),
    path('agents/<int:agent_id>/remove-gadget/<int:gadget_id>/', views.remove_gadget, name='remove-gadget'),
    
    # # Mission-Agent Association/removal
    path('missions/<int:mission_id>/associate-agent/<int:agent_id>/', views.associate_agent, name='associate-agent'),
    path('missions/<int:mission_id>/remove-agent/<int:agent_id>/', views.remove_agent, name='remove-agent'),
    
    # Sign up route
    path('accounts/signup/', views.signup, name='signup'),
]