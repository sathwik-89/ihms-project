from django import forms
from django.contrib.auth.models import User
from .models import PatientProfile, DoctorProfile, Appointment, MedicalRecord, Bill

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ['address', 'phone', 'blood_group', 'dob']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ['specialization', 'consultation_fee', 'phone']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'appointment_date', 'reason']
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['diagnosis', 'prescription']

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['amount']
