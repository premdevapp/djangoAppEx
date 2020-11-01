from django import forms
from fbvApp.models import Student

# Create your forms here.

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
