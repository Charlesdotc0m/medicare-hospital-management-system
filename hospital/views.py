from django.shortcuts import render
from .forms import PatientForm, AppointmentForm
from django.contrib import messages
from .models import Department, Doctor, Patient, Appointment

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def department(request):
    departments = Department.objects.all()
    return render(request, 'department.html', {'departments': departments})


def doctor(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor.html', {'doctors': doctors})


def register(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Patient Registered Successfully!")
            form = PatientForm()

    else:
        form = PatientForm()

    return render(request, 'register.html', {'form': form})


def appointments(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Appointment Booked Successfully!")
            form = AppointmentForm()

    else:
        form = AppointmentForm()

    return render(request, 'appointments.html', {'form': form})


def contact(request):
    return render(request, 'contact.html')

def dashboard(request):
    context = {
        'doctor_count': Doctor.objects.count(),
        'department_count': Department.objects.count(),
        'patient_count': Patient.objects.count(),
        'appointment_count': Appointment.objects.count(),
    }

    return render(request, 'dashboard.html', context)