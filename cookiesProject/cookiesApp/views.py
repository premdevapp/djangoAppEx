from django.shortcuts import render
from django.http import HttpResponse
from .forms import ItemForm

# Create your views here.
def home(request):
    request.session.set_test_cookie()
    return HttpResponse('<h2>Home Page</h2>')

def page(request):
    if request.session.test_cookie_worked():
        print('cookies are enabled')
    request.session.delete_test_cookie()
    return HttpResponse('<strong>Page with or without Cookie</strong>')

def CountView(request):
    if 'total' in request.COOKIES:
        total = int(request.COOKIES['total']) + 1
    else:
        total = 1
    response = render(request, 'cookiesApp/count.html', {'total': total})
    response.set_cookie('total', total)
    return response

def index(request):
    return render(request, 'cookiesApp/index.html')

def addItem(request):
    form = ItemForm()
    response = render(request, 'cookiesApp/addItem.html', {'form': form})
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            response.set_cookie(name, quantity, 120)
    return response

def displayCart(request):
    return render(request, 'cookiesApp/displayItems.html')