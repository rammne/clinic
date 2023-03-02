from django import forms
from .models import Patient, Record, Permissions

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

class PermissionsForm(forms.ModelForm):
    class Meta:
        model = Permissions
        fields = ['vax', 'date_given', 'c1', 'c2', 'c3', 'c4', 'hospital', 'allergy', 'remarks', 'parents_name', 'date_printed']