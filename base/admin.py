from django.contrib import admin
from .models import Patient

admin.site.register(Patient)
admin.site.site_header = "OLOPSC"
admin.site.site_title = "CLINIC"