from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def displayQuotes(request):
    return HttpResponse('The best investment we can make in ourself')

