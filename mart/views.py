from django.shortcuts import render, redirect
from django.urls import reverse
from products.models import Product

def index(request):
    products = Product.objects.filter(active=True)
    
    if request.method == 'POST':
        selected_product_ids = request.POST.getlist('selected_products')
        query_string = '&'.join([f'product_ids={id}' for id in selected_product_ids])
        return redirect(f'{reverse("mart")}?{query_string}')
    
    return render(request, 'home.html', {'products': products})

def mart(request):
    selected_product_ids = request.GET.getlist('product_ids')
    
    selected_products = Product.objects.filter(id__in=selected_product_ids, active=True)
    
    return render(request, 'mart/mart.html', {'selected_products': selected_products})
