from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('wishlists/', views.wishListList, name='all wishlists'),
    path('wishlists/<int:id>/', views.wishListDetail, name='detail wish list'),
    path('wishlists/mappoints/', views.mapAnnotationPoint, name='post map point'),
    path('wishlists/mappoints/<int:id>/', views.mapPointDetail, name='detail map point')
]