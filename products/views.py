import uuid
from django.shortcuts import render, get_object_or_404
from .models import Product,Tracking
from django.shortcuts import render, redirect



# Create your views here.
def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product.html', {'product': product})

def products(request):
    products = Product.objects.filter(active=True)
    return render(request, 'products/products.html', {'products': products})



def add_to_tracking(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    tracking_entry, created = Tracking.objects.get_or_create(
        user=request.user, product=product,
        defaults={'tracking_id': str(uuid.uuid4()), 'status': 'pending'}
    )

    return redirect('view_tracking')

def view_tracking(request):
    tracking_entries = Tracking.objects.filter(user=request.user)

    return render(request, 'tracking.html', {'tracking_entries': tracking_entries})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', [])

    if product_id not in cart:
        cart.append(product_id)
        request.session['cart'] = cart  

    return redirect('view_cart')  

def view_cart(request):
    cart = request.session.get('cart', [])

    cart_products = Product.objects.filter(id__in=cart, active=True)

    return render(request, 'cart.html', {'cart_products': cart_products})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])

    if product_id in cart:
        cart.remove(product_id)
        request.session['cart'] = cart  

    return redirect('view_cart')