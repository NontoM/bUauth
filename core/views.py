from django.shortcuts import render
from django.shortcuts import get_object_or_404


# Create your views here.

def home(request):
    return render(request, 'home.html')
    