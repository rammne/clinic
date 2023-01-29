from django.db import models
from django.urls import reverse

class Patient(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="First name")
    last_name = models.CharField(max_length=50, verbose_name="Last name")
    middle_name = models.CharField(max_length=50, blank=True, verbose_name="Middle name")
    grade_year_level = models.CharField(max_length=50, null=True, blank=True, verbose_name="Grade/Year Level")
    section = models.CharField(max_length=50, null=True, blank=True, verbose_name="Section")

    MALE = 'M'
    FEMALE = 'F'

    CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

    sex = models.CharField(choices=CHOICES, default=MALE, max_length=1, verbose_name="Sex")
    student_number = models.CharField(max_length=10, default='00x-0000', verbose_name="Student Number")
    age = models.CharField(max_length=20, null=True, verbose_name="Age")
    date_of_birth = models.CharField(max_length=50, verbose_name="Date of birth", null=True, blank=True)
    patient_address = models.CharField(max_length=100, verbose_name="Address")
    patient_contact = models.CharField(max_length=15, verbose_name="Telephone/Cellphone number", null=True, blank=True)
    guardian = models.CharField(max_length=50, blank=True, verbose_name="Guardian")
    guardian_address = models.CharField(max_length=100, blank=True, verbose_name="Guardian's address")
    guardian_telephone = models.CharField(max_length=15, blank=True, verbose_name="Guardian's Telephone/Cellphone number")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    

    

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.middle_name


    def get_absolute_url(self):
        return reverse('patient-detail', kwargs={'pk' : self.pk})

class Illness(models.Model):
    illness_name = models.CharField(max_length=20, verbose_name="Illness name", null=True, blank=True)
    past = models.CharField(max_length=50, verbose_name="Past medical history", null=True, blank=True)
    present = models.CharField(max_length=50, verbose_name="Current medical condition", null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Patient", related_name='illness')
    
    def __str__(self):
        return self.illness_name

    def get_absolute_url(self):
        return reverse('patient-details', kwargs={'pk' : self.pk})

class PatientData(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="data")
    height = models.DecimalField(null=True, blank=True, max_digits=4, decimal_places=1, verbose_name="Height (cm)")
    weight = models.DecimalField(null=True, blank=True, max_digits=4, decimal_places=1, verbose_name="Weight (kg)")
    eyes = models.CharField(null=True, blank=True, max_length=20, verbose_name="Eyes")
    r_vision = models.CharField(null=True, blank=True, max_length=20, verbose_name="Right Vision")
    l_vision = models.CharField(null=True, blank=True, max_length=20, verbose_name="Left Vision")
    ears = models.CharField(null=True, blank=True, max_length=20, verbose_name="Ears")
    nose = models.CharField(null=True, blank=True, max_length=20, verbose_name="Nose")
    throat = models.CharField(null=True, blank=True, max_length=20, verbose_name="Throat")
    mouth = models.CharField(null=True, blank=True, max_length=20, verbose_name="Mouth")
    neck = models.CharField(null=True, blank=True, max_length=20, verbose_name="Neck")
    extremities = models.CharField(null=True, blank=True, max_length=20, verbose_name="Extremities")
    heart_auscultation = models.CharField(null=True, blank=True, max_length=20, verbose_name="Heart Auscultation")
    lung_auscultation = models.CharField(null=True, blank=True, max_length=20, verbose_name="Lung Auscultation")
    skin = models.CharField(null=True, blank=True, max_length=20, verbose_name="Skin")
    nails = models.CharField(null=True, blank=True, max_length=20, verbose_name="Nails")
    head = models.CharField(null=True, blank=True, max_length=20, verbose_name="Head")
    personal_hygiene = models.CharField(null=True, blank=True, max_length=20, verbose_name="Personal Hygiene")
    general_health = models.CharField(null=True, blank=True, max_length=20, verbose_name="General Health")
    other_remarks = models.TextField(null=True, blank=True, verbose_name="Other Remarks")
    name_of_physician = models.CharField(null=True, blank=True, max_length=20, verbose_name="Name of Physician")

    SATISFACTION = 'O'
    REQUIRES_ATTENTION = 'X'
    PARENTS_NOTIFIES = 'P'

    RATING = (
        (SATISFACTION, 'Satisfaction'),
        (REQUIRES_ATTENTION, 'Requires attention'),
        (PARENTS_NOTIFIES, 'Parents notified'),
    )

    code_of_rating = models.CharField(choices=RATING, default=SATISFACTION, verbose_name="Code of Rating", max_length=1)


class Record(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='records')
    chief_complains = models.CharField(max_length=50)
    action = models.CharField(max_length=100, null=True, blank=True)
    treatments_medication = models.CharField(max_length=50, null=True, blank=True)
    remarks = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient.first_name + ' ' + self.chief_complains

    def get_absolute_url(self):
        return reverse('patient-records', kwargs={'pk' : self.pk})


'''class VisitorsLogs(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    student_number = models.CharField(max_length=20)
    year_or_level = models.CharField(max_length=20)
    program = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name'''