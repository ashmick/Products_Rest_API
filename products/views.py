from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProductSerializer
from .models import Products
from rest_framework import status
from django.shortcuts import get_object_or_404



# Create your views here.
@api_view (['GET', 'POST'])
def products_list(request):
    if request.method == 'GET':
        product=Products.objects.all()
        serializer= ProductSerializer(product, many=True)
        return Response(serializer.data)
    
    elif request.method== 'POST':
        serializer= ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view (['GET'])
def product_detail (request,pk):
    try:
        product=Products.objects.get(pk=pk)
        serializer= ProductSerializer(product)
        return Response (serializer.data)
    
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND);