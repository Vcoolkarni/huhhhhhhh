from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Model for Patients
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    phone_number = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username

# Model for Doctors
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    specialty = models.CharField(max_length=100)
    medical_license_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"Dr. {self.user.username}"

# Model for Medicines
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

# Model for Pharmacies
class Pharmacy(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    medicines = models.ManyToManyField(Medicine, related_name='pharmacies')

    def __str__(self):
        return self.name

# Model for Prescriptions
class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='prescriptions')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='prescriptions')
    medicines = models.ManyToManyField(Medicine)
    diagnosis = models.TextField(blank=True)
    prescription_text = models.TextField()
    date_prescribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.patient.user.username}"

# Model for Appointments
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    appointment_time = models.DateTimeField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Appointment with Dr. {self.doctor.user.username} for {self.patient.user.username}"