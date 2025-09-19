from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import PatientSerializer, DoctorSerializer
from .models import Patient, Doctor

# ViewSet for the Patient model
class PatientViewSet(viewsets.ModelViewSet):
    # 'queryset' is what tells the view which data to display.
    # .objects.all() gets all the Patient objects from the database.
    queryset = Patient.objects.all()
    # 'serializer_class' is what tells the view which serializer to use
    # to convert the data to JSON.
    serializer_class = PatientSerializer

# ViewSet for the Doctor model
class DoctorViewSet(viewsets.ModelViewSet):
    # 'queryset' gets all the Doctor objects from the database.
    queryset = Doctor.objects.all()
    # 'serializer_class' tells the view to use the DoctorSerializer.
    serializer_class = DoctorSerializer