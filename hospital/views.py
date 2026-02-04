from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import UserRegistrationForm, PatientProfileForm, DoctorProfileForm, AppointmentForm, MedicalRecordForm, BillForm
from .models import PatientProfile, DoctorProfile, Appointment, Bill, MedicalRecord

def home(request):
    return render(request, 'hospital/home.html')

def signup_patient(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = PatientProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            patient_group, created = Group.objects.get_or_create(name='Patient')
            user.groups.add(patient_group)
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            login(request, user)
            return redirect('patient_dashboard')
    else:
        user_form = UserRegistrationForm()
        profile_form = PatientProfileForm()
    return render(request, 'hospital/signup_patient.html', {'user_form': user_form, 'profile_form': profile_form})

def signup_doctor(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = DoctorProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            doctor_group, created = Group.objects.get_or_create(name='Doctor')
            user.groups.add(doctor_group)
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            login(request, user)
            return redirect('doctor_dashboard')
    else:
        user_form = UserRegistrationForm()
        profile_form = DoctorProfileForm()
    return render(request, 'hospital/signup_doctor.html', {'user_form': user_form, 'profile_form': profile_form})

def login_redirect(request):
    if request.user.groups.filter(name='Doctor').exists():
        return redirect('doctor_dashboard')
    elif request.user.groups.filter(name='Patient').exists():
        return redirect('patient_dashboard')
    elif request.user.is_superuser:
         return redirect('/admin/')
    else:
        return redirect('home') # Fallback

@login_required
def patient_dashboard(request):
    if not hasattr(request.user, 'patientprofile'):
        return redirect('home')
    appointments = Appointment.objects.filter(patient=request.user.patientprofile).order_by('-appointment_date')
    return render(request, 'hospital/patient_dashboard.html', {'appointments': appointments})

@login_required
def doctor_dashboard(request):
    if not hasattr(request.user, 'doctorprofile'):
        return redirect('home')
    appointments = Appointment.objects.filter(doctor=request.user.doctorprofile).order_by('appointment_date')
    return render(request, 'hospital/doctor_dashboard.html', {'appointments': appointments})

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user.patientprofile
            appointment.save()
            return redirect('patient_dashboard')
    else:
        form = AppointmentForm()
    return render(request, 'hospital/book_appointment.html', {'form': form})

@login_required
def update_appointment_status(request, pk, status):
    if not hasattr(request.user, 'doctorprofile'):
        return redirect('home')
    appointment = get_object_or_404(Appointment, pk=pk)
    if appointment.doctor == request.user.doctorprofile:
        appointment.status = status
        appointment.save()
        if status == 'completed':
            return redirect('add_medical_record', pk=appointment.pk)
    return redirect('doctor_dashboard')

@login_required
def add_medical_record(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        record_form = MedicalRecordForm(request.POST)
        bill_form = BillForm(request.POST)
        if record_form.is_valid() and bill_form.is_valid():
            record = record_form.save(commit=False)
            record.appointment = appointment
            record.save()
            
            bill = bill_form.save(commit=False)
            bill.appointment = appointment
            bill.save()
            return redirect('doctor_dashboard')
    else:
        record_form = MedicalRecordForm()
        bill_form = BillForm()
    return render(request, 'hospital/add_medical_record.html', {'record_form': record_form, 'bill_form': bill_form, 'appointment': appointment})

@login_required
def view_medical_history(request):
    # For patient
    records = MedicalRecord.objects.filter(appointment__patient=request.user.patientprofile)
    return render(request, 'hospital/medical_history.html', {'records': records})

@login_required
def view_bills(request):
    bills = Bill.objects.filter(appointment__patient=request.user.patientprofile)
    return render(request, 'hospital/view_bills.html', {'bills': bills})
