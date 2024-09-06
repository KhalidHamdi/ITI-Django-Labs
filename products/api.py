from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def products_api (request):
    products = Product.objects.filter(active=True)
    
    serializer = ProductSerializer(products, many=True)   
    return Response(serializer.data)

@api_view(['GET'])
def product_api (request, product_id):
    product = get_object_or_404(Product, id=product_id)
    serializer = ProductSerializer(product)
    
    return Response(serializer.data)