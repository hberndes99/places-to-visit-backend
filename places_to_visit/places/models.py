from django.db import models
from django.db.models.fields.related import ForeignKey
# dango has built in ORM
# db structure represented as classes



class WishList(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MapAnnotationPoint(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    latitude = models.IntegerField()
    longitude = models.IntegerField
    number = models.CharField(max_length=10)
    streetAddress = models.CharField(max_length=50)
    wishList = models.ForeignKey(WishList, on_delete=models.CASCADE)

    def __str__(self):
        return self.title