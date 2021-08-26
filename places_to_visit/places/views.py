from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('<h1>hello</h1>')




#GET all map points
# '/'

#GET all wish lists
# '/wishlists'

#GET map points for a specified wish list
# '/wishlists/id/savedplaces'

#POST new wish list
# '/wishlists'

#POST new map annotation point, related to a specific wish list
# '/wishlists/id/savedplaces

#DELETE wish list and all related map points
# '/wishlists/id

#DELETE map point from specific wish list
# '/wishlists/id/savedplaces/id