from django.shortcuts import render
from django.http import HttpResponse
import datetime
from string import Template

# Create your views here.
def display(request):
    return HttpResponse('<h1>my FBV django app</h1>')

def displayDateTime(request):
    dt = datetime.datetime.now()
    templ = Template('Current date is $date and time is $time')
    str = templ.substitute(date=dt.strftime("%A %d %B %Y"), time =dt.strftime("%I:%M %p"))
    s = '<strong> '+ str + '</strong>'
    return HttpResponse(s)

