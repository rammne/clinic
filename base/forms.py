from django import forms
from .models import Patient, VisitorsLogs

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class VisitorsLogsForm(forms.ModelForm):
    class Meta:
        model = VisitorsLogs
        fields = '__all__'