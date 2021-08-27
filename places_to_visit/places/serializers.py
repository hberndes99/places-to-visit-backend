from .models import WishList, MapAnnotationPoint
from rest_framework import serializers


class MapAnnotationPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapAnnotationPoint
        fields = '__all__'

class WishListSerializer(serializers.ModelSerializer):

    items = MapAnnotationPointSerializer(many=True, read_only=True)
    class Meta:
        model = WishList
        fields = ['id', 'name', 'description', 'items']

        def create(self, validated_data):
            items_data = validated_data.pop('items')
            wishList = WishList.objects.create(**validated_data)
            for item_data in items_data:
                MapAnnotationPoint.objects.create(wishList=wishList, **item_data)
            return wishList

