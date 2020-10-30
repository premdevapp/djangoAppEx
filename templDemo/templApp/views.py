from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    myDict = {"name": "premnath"}
    return render(request, 'templApp/firstTemplate.html', context=myDict)

def renderEmp(request):
    myDict = {"ID": 345154351, "name": "Jhon", "salary": 10000}
    return render(request, 'templApp/employeeTemplate.html', context=myDict)