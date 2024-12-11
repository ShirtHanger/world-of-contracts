from django.contrib import admin
from .models import Agent, Gadget, Mission

# Register your models here for Admin CRUD

admin.site.register(Agent)
admin.site.register(Gadget)
admin.site.register(Mission) 