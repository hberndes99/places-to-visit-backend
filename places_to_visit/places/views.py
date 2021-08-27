
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers
from .models import WishList, MapAnnotationPoint

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import WishListSerializer


# Create your views here.
def hello(request):
    return HttpResponse('<h1>hello</h1>')




#GET all map points
# '/'

#GET all wish lists
# '/wishlists'
@api_view(['GET'])
def wishListList(request):
    wishLists = WishList.objects.all()
    serializer = WishListSerializer(instance=wishLists, many=True)
    return Response(serializer.data)


