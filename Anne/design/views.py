from django.shortcuts import render

# Create your views here.
from Anne import settings

def design(request):
    return render(request,'design.html')


