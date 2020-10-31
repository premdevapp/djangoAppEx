from django.shortcuts import render
from . import forms

# Create your views here.
def userRegisterationView(request):
    form = forms.UserRegisterationForm()
    if request.method == 'POST':
        form = forms.UserRegisterationForm(request.POST)
        if form.is_valid():
            print('FORm IS VALID')
            print('First Name', form.cleaned_data['firstName'])
            print('last Name', form.cleaned_data['lastName'])
            print('email', form.cleaned_data['email'])
            print('gender', form.cleaned_data['gender'])

    return render(request, 'formApp/userregisteration.html', {'form':form})
