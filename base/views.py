from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from rest_framework import serializers

@api_view(['GET'])
def index(req):
    return Response({'msg':'hello'})



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


@api_view(['GET'])
def Products(req):
    pro_Product=Product.objects.all()
    return Response (ProductSerializer(pro_Product,many=True).data)

@api_view(['POST'])
def addproduct(req):     
    pro_Product = ProductSerializer(data=req.data)
    if pro_Product.is_valid():
            pro_Product.save()
            return Response ("post...")

@api_view(['DELETE'])
def delproduct(req,id=-1):
    pro_Product=Product.objects.get(id=id)
    pro_Product.delete()
    return Response ("del...")