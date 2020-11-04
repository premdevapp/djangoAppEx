from django.db import models

# Create your models here.

class Patient(models.Model):
    lastName = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    age = models.IntegerField()

class ClinicalData(models.Model):
    COMPONENT_NAME = [('hw', 'Height/Weight'), ('bp', 'Blood Pressure'), ('hr', 'Heart Rate')]
    componentName = models.CharField(choices=COMPONENT_NAME ,max_length=20)
    componentValue = models.CharField(max_length=20)
    measuredDateTime = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)