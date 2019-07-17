from django.contrib import admin
from .models import Event, UserProfile, Club, EventRegistration, EventAttendance

admin.site.register(Event)
admin.site.register(UserProfile)
admin.site.register(Club)
admin.site.register(EventRegistration)
admin.site.register(EventAttendance)

