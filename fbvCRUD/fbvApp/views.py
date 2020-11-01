from django.shortcuts import render, redirect
from fbvApp.models import Student
from fbvApp.forms import StudentForm

# Create your views here.

def getStudents(request):
    students = Student.objects.all()
    return render(request, 'fbvApp/index.html', {'students':students})

def createStudent(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/fbvapp/')
    return render(request, 'fbvApp/create.html', {'form': form})