from django.contrib import admin
from EnergyWebsite.models import Energy, Date, Fossil, Renewable
# Register your models here.

admin.site.register(Energy)
admin.site.register(Date)
admin.site.register(Fossil)
admin.site.register(Renewable)