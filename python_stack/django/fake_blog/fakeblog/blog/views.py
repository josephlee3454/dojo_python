from django.shortcuts import HttpResponse, redirect # add redirect to import statement
from django.http import JsonResponse


def root_method(request):
    return HttpResponse("this the home placeholder")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def blog_num(request, my_val):	# my_val would be a number from the URL
    return HttpResponse(f"placeholder to display blog number {my_val}")

def edit(request, my_val):	# my_val would be a number from the URL
    return HttpResponse(f"placeholder to edit blog {my_val}")

def delete(request):
    return redirect("/")

def json_rep(request):

    # do something with the your data
    data = {   
    "name":"John W", 
    "actually is ": "the fake space panda" 
    }

    # just return a JsonResponse
    return JsonResponse(data)
