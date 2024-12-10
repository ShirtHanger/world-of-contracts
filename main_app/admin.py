from django.contrib import admin
from .models import Agent, Gadget#, Mission

# Register your models here for Admin CRUD

admin.site.register(Agent)
# admin.site.register(Mission) 
admin.site.register(Gadget)