from django.urls import path,include
from . import views

urlpatterns = [
    
    
    path("__reload__/", include("django_browser_reload.urls")),
]
