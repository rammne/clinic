from django.contrib import admin
from .models import Patient, PatientDiagnostic

admin.site.register(Patient)
admin.site.register(PatientDiagnostic)
admin.site.site_header = "OLOPSC"
admin.site.site_title = "CLINIC"