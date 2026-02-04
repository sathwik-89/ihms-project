# Integrated Hospital Management System (IHMS)

A comprehensive web-based Hospital Management System built with Django.

## Features
- **Patient Module**: Registration, Login, Book Appointments, View Medical History, View Bills.
- **Doctor Module**: Login, View Appointments, Approve/Reject Appointments, Add Medical Records & Diagnosis.
- **Billing Module**: Automated bill generation, Payment status tracking.
- **Admin Panel**: Full control over users, appointments, records, and bills.

## Tech Stack
- Python 3.x
- Django 5.x
- SQLite3
- HTML5, CSS3

## Installation

1. **Clone the repository** (or download the project folder).

2. **Navigate to the project directory**:
   ```bash
   cd ihms_project
   ```

3. **Install Django (if not installed)**:
   ```bash
   pip install django
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create Superuser (Admin)**:
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set username and password.

6. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**:
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Usage Guide or "Happy Path"

1. **Admin Setup**: Login to `/admin/` and create some initial data if needed, or just manage the system.
2. **Patient**:
   - Generic visitors go to Home page.
   - Click "I am a Patient" to sign up.
   - Login and book an appointment with a doctor.
3. **Doctor**:
   - Click "I am a Doctor" to sign up.
   - Login to see assigned appointments.
   - Approve an appointment.
   - Once the appointment is done, click "Complete & Add Record" to add diagnosis and generate bill.
4. **Patient** (Again):
   - Login to see appointment status 'Approved' or 'Completed'.
   - View Medical History and Bills.

## Credentials
- **Admin**: Log in with the superuser you created.
- **Users**: Register via the signup forms.
