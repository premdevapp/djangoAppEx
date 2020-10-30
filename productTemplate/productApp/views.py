from django.shortcuts import render

# Create your views here.
def electronics(request):
    product_dict = {'product1':'mac', 'product2':'iphone', 'product3':'dell'}
    return render(request, 'productApp/productinfo.html', context=product_dict)

def toys(request):
    product_dict = {'product1':'remote car', 'product2':'drones', 'product3':'rocket'}
    return render(request, 'productApp/productinfo.html', context=product_dict)

def shoes(request):
    product_dict = {'product1':'niki', 'product2':'adadas', 'product3':'rebook'}
    return render(request, 'productApp/productinfo.html', context=product_dict)

def index(request):
    return render(request, 'productApp/index.html')