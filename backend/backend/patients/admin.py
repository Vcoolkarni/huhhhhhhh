from django.contrib import admin
from .models import Patient, Doctor, Pharmacy, Medicine, Prescription, Appointment

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Pharmacy)
admin.site.register(Medicine)
admin.site.register(Prescription)
admin.site.register(Appointment)