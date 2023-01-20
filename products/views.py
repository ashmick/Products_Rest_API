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
    
    
@api_view (['GET', 'PUT', 'DELETE'])
def product_detail (request, pk):
    Products=get_object_or_404(Products, pk=pk)
    
    if request.method=='GET':
        serializer=ProductSerializer(Products)
        return Response(serializer.data)
    

    elif request.method=='PUT':
        serializer=ProductSerializer(Products, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    
    elif request.method=='DELETE':
        product_detail()
        return Response(status=status.HTTP_204_NO_CONTENT)