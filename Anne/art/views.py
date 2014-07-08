from django.shortcuts import render

# Create your views here.
from Anne import settings

def art(request):
    return render(request,'art.html')
