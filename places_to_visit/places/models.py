from django.db import models
from django.db.models.fields.related import ForeignKey
# dango has built in ORM
# db structure represented as classes

class WishList(models.Model):
    name = models.CharField(max_length=30)
    #items = models.ForeignKey(MapAnnotationPoint)
    description = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class MapAnnotationPoint(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=20, decimal_places=17)
    longitude = models.DecimalField(max_digits=20, decimal_places=17)
    number = models.CharField(max_length=10)
    streetAddress = models.CharField(max_length=50)
    wishList = models.ForeignKey(WishList, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.title



