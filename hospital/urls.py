from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/patient/', views.signup_patient, name='signup_patient'),
    path('signup/doctor/', views.signup_doctor, name='signup_doctor'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('redirect/', views.login_redirect, name='login_redirect'),
    
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('patient/book-appointment/', views.book_appointment, name='book_appointment'),
    path('patient/medical-history/', views.view_medical_history, name='view_medical_history'),
    path('patient/bills/', views.view_bills, name='view_bills'),

    path('doctor/dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('doctor/appointment/<int:pk>/status/<str:status>/', views.update_appointment_status, name='update_appointment_status'),
    path('doctor/appointment/<int:pk>/record/', views.add_medical_record, name='add_medical_record'),
]
