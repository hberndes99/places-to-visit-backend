from .models import WishList, MapAnnotationPoint
from rest_framework import serializers


class MapAnnotationPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapAnnotationPoint
        fields = '__all__'

class WishListSerializer(serializers.ModelSerializer):

    items = MapAnnotationPointSerializer(many=True)
    class Meta:
        model = WishList
        fields = ['id', 'name', 'description', 'items']



