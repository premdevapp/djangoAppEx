from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from cvbApp.models import Student
from django.urls import reverse_lazy

# Create your views here.
class StudentListView(ListView):
    model = Student
    #default template_name is student_list.html
    #default context_object_name is student_list

class StudentDetailView(DetailView):
    model = Student
    #default template_name is student_detail.html
    #default context_object_name is student

class StudentCreateView(CreateView):
    model = Student
    fields = ('firstName', 'lastName', 'testScore')
    #default template_name is student_form.html
    #default context_object_name is form

class StudentUpdateView(UpdateView):
    model = Student
    fields = ('testScore',)
    #default template_name is student_form.html
    #default context_object_name is form

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students')
    #default template_name is student_form.html
    #default context_object_name is form