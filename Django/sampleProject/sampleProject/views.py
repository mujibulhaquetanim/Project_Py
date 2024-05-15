from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from the home page")

def contact(request):
    return HttpResponse("Hello from contact page")

def about(request):
    return HttpResponse("Hi from the about page")