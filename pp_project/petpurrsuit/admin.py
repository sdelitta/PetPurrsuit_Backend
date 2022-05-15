from django.contrib import admin

from django.contrib import admin
from .models import State, Shelter, Canine, Feline

admin.site.register(State)
admin.site.register(Shelter)
admin.site.register(Canine)
admin.site.register(Feline)
