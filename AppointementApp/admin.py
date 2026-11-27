from django.contrib import admin
from AppointementApp.models import Appointment

# Register your models here.
@admin.site.register(Appointment)
class appointmentAdminPersonaliser(admin.ModelAdmin):
    