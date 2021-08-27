from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('wishlists/', views.wishListList, name='all wishlists'),
    path('wishlists/mappoints/', views.mapAnnotationPoint, name='post map point')
]