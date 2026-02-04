from django.contrib import admin
from .models import PatientProfile, DoctorProfile, Appointment, MedicalRecord, Bill

@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'blood_group', 'dob')
    search_fields = ('user__username', 'phone')

@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'consultation_fee')
    search_fields = ('user__username', 'specialization')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_date', 'status')
    list_filter = ('status', 'appointment_date')
    search_fields = ('patient__user__username', 'doctor__user__username')

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'created_at')
    search_fields = ('appointment__patient__user__username',)

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('appointment', 'amount', 'is_paid')
    list_filter = ('is_paid',)
