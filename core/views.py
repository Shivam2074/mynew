from django.shortcuts import render, HttpResponse

# Create your views here.

def print(request):
    return HttpResponse("This is my world.")
