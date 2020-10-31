from django.shortcuts import render
from modelFormApp.forms import ProjectForm
from modelFormApp.models import Project

# Create your views here.
def index(request):
    return render(request, 'modelFormApp/index.html');

def listProjects(request):
    projectsList = Project.objects.all()
    return render(request, 'modelFormApp/listprojects.html', {'projects':projectsList})

def addProjects(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request) 
    return render(request, 'modelFormApp/addproject.html', {'form':form})