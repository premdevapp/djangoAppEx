from django.shortcuts import render
from .forms import ItemForm
from django.http import HttpResponse

# Create your views here.
def pageCount(request):
    count = request.session.get('count', 0)
    count += 1
    request.session['count'] = count
    return render(request, 'sessionApiApp/count.html', {'count': count})

def index(request):
    request.session.set_expiry(180)
    del request.session['count']
    return render(request, 'sessionApiApp/index.html')

def addItem(request):
    form = ItemForm()
    response = render(request, 'sessionApiApp/addItem.html', {'form': form})
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        request.session[name] = quantity
    return response

def displayCart(request):
    return render(request, 'sessionApiApp/displayItems.html')
