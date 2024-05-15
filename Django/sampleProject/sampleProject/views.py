from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')
    # return HttpResponse("Hello from the home page")

def contact(request):
    # return HttpResponse("Hello from contact page")
    return render(request, 'website/contact.html')

def about(request):
    # return HttpResponse("Hi from the about page")
    return render(request, 'website/about.html')