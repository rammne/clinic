from .models import Patient, VisitorsLogs, Record
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PatientForm, VisitorsLogsForm
from django.urls import reverse
from django.db.models import Q
from django.http import HttpResponseRedirect

def home(request):
    query = request.GET.get('q') if request.GET.get('q') != None else ''
    patients = Patient.objects.filter(  Q(first_name__icontains=query) |
                                        Q(last_name__icontains=query) |
                                        Q(student_number__icontains=query))

    return render(request, 'base/home.html', {'patients':patients})

def patient_form(request):
    form = PatientForm()

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PatientForm()

    return render(request, 'base/patient_form.html', {'form': form})

def patient_form_update(request, pk):
    patient = get_object_or_404(Patient, id=pk)
    form = PatientForm(request.POST or None, instance=patient)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('patient-details', args=[patient.pk]))

    context = {'patient': patient, 'form':form}
    return render(request, 'base/patient_form.html', context)

def patient_details(request, pk):
    patient = get_object_or_404(Patient, id=pk)
    illness_obj = patient.illness.all()
    logs = VisitorsLogs.objects.filter(first_name='Rammne', last_name='Tiongson').first()

    if request.method == 'POST':
        if request.POST.get('illness'):
            patient.illness.create(illness_name=request.POST.get('illness'), past=request.POST.get('past'), present=request.POST.get('present'))
            return redirect(reverse('patient-details', args=[patient.pk]))

        delete_obj = list(request.POST.keys())

        if request.POST[delete_obj[1]] == 'Delete':
            patient.illness.filter(pk=delete_obj[1]).delete()
            
    return render(request, 'base/patient_details.html', {'patient':patient, 'illness_obj':illness_obj, 'logs':logs})

def delete_patient(request, pk):

    if request.META.get('HTTP_REFERER') == 'http://127.0.0.1:8000/':
        patient = get_object_or_404(Patient, id=pk)
        patient.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def patient_data(request, pk):
    patient = get_object_or_404(Patient, id=pk)
    patient_data = patient.data.all()

    if not patient_data:
        patient.data.create(height=1.0)
        return redirect(reverse('patient-data', args=[patient.pk]))

    if request.method == 'POST':
            patient.data.update_or_create(patient=patient.id, defaults={list(request.POST)[1]:request.POST[list(request.POST)[1]]})
            return redirect(reverse('patient-data', args=[patient.pk]))
    context = {'patient': patient, 'patient_data':patient_data}

    return render(request, 'base/patient_data.html', context)

def patient_logs(request):

    query = request.GET.get('q') if request.GET.get('q') != None else ''
    obj = VisitorsLogs.objects.filter(  Q(first_name__icontains=query) |
                                        Q(last_name__icontains=query) |
                                        Q(student_number__icontains=query))
    form = VisitorsLogsForm()

    if request.method == 'POST':
        form = VisitorsLogsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient-logs')
        else:
            form = VisitorsLogsForm()

        if request.POST.get('delete'):
            obj_id = request.POST.get('delete')
            VisitorsLogs.objects.get(id=obj_id).delete()

    context = {'obj':obj, 'form':form}

    return render(request, 'base/patient_logs.html', context)

def patient_records(request, pk):
    patient = get_object_or_404(Patient, id=pk)
    p_records = patient.records.all()

    if request.method == 'POST' and not request.POST.get('delete'):
        patient.records.create(chief_complains=request.POST.get('chief_complains'),
                                treatments_medication=request.POST.get('treaments_medication'),
                                remarks=request.POST.get('remarks'),)

    if request.POST.get('delete'):
        patient.records.get(id=request.POST.get('delete')).delete()
        return redirect(reverse('patient-records', args=[patient.pk]))

    context = {'p_records':p_records}

    return render(request, 'base/patient_records.html', context)