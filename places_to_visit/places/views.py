
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers
from .models import WishList, MapAnnotationPoint

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import MapAnnotationPointSerializer, WishListSerializer

import json


# Create your views here.
def hello(request):
    return HttpResponse('<h1>hello</h1>')


#GET all wish lists
#POST new wish list
# '/wishlists'
@api_view(['GET', 'POST'])
def wishListList(request):
    if request.method == 'GET':
        wishLists = WishList.objects.all()
        serializer = WishListSerializer(instance=wishLists, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        serializer = WishListSerializer(data=data, many=False)
        if serializer.is_valid():
            print('valid')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#wishlists/id
@api_view(['DELETE'])
def wishListDetail(request, id):
    try:
        wishList = WishList.objects.get(pk=id)
    except:
        return Response({'message': 'The place does not exist'}, status=status.HTTP_404_NOT_FOUND)
    wishList.delete()
    return Response({'message': 'Successfully deleted wish list'}, status=status.HTTP_204_NO_CONTENT)

#/wishLists/mappoints
@api_view(['POST'])
def mapAnnotationPoint(request):
    data = json.loads(request.body)
    print(data)
    serializer = MapAnnotationPointSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#/wishlists/mapoints/id
@api_view(['DELETE'])
def mapPointDetail(request, id):
    try: 
        mapPoint = MapAnnotationPoint.objects.get(pk=id)
    except: 
        return Response({'message': 'The place does not exist'}, status=status.HTTP_404_NOT_FOUND)
    mapPoint.delete()
    return Response({'message': 'Successfully deleted map point'}, status=status.HTTP_204_NO_CONTENT)


