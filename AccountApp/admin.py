from django.contrib import admin
from AccountApp.models import Doctor, Patient, Speciality,User
 

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(User)
admin.site.register(Speciality)