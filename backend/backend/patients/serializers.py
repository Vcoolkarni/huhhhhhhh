from rest_framework import serializers
from .models import Patient, Doctor

# Serializer for the Patient model
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__' # Use all fields from the Patient model

# Serializer for the Doctor model
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__' # Use all fields from the Doctor model