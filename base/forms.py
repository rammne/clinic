from django import forms
from .models import Patient, Record

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['chief_complains', 'action', 'treatments_medication', 'remarks']


'''class VisitorsLogsForm(forms.ModelForm):
    class Meta:
        model = VisitorsLogs
        fields = '__all__'''