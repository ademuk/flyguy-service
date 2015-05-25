from django.contrib import admin
from .models import Flight


class FlightAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'notes')
    ordering = ('-date',)

admin.site.register(Flight, FlightAdmin)

