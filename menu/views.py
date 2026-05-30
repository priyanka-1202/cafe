from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

items = [
    {'id' : 1,
     'food' : 'burger',
     'price' : 120,
     'details' : 'patty in buns with sauce'},
    {'id' : 2,
     'food' : 'pizza',
     'price' : 150,
     'details' : 'circular bread with toppics and sauce'},
    {'id' : 3,
     'food' : 'coffee',
     'price' : 90,
     'details' : 'sweet drink make of coffe beans and milk'},
]

def home(request):
    username = {'fname' : 'Priyanka',
                'lname' : 'Kapale'}
    return render(request, "menu/home.html", context = {"username" : username})

def menu(request):
    return render(request, "menu/menu.html", context = {"items" : items})

#showing single post
def food(request, id):
    for item in items:
        if item['id'] == id:
            return render(request, "menu/food.html", context={'item' : item}) 
    return HttpResponseNotFound("Food details not available")


