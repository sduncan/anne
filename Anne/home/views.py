from django.shortcuts import render

# Create your views here.
from Anne import settings

def home(request):
    return render(request,'home.html')


