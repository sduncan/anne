from django.shortcuts import render

# Create your views here.
from Anne import settings

def photography(request):
    return render(request,'photo.html')
