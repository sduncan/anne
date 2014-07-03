from django.shortcuts import render

# Create your views here.
from Anne import settings

def home(request):
    return render(request,'home.html')

def photo(request):
    return render(request,'photo.html')

def art(request):
    return render(request,'art.html')

def design(request):
    return render(request,'design.html')

def contact(request):
    return render(request,'contact.html')

def anneadminlogin(request):
    return render(request,'login.html')

def anneadmin(request):
    return render(request,'admin.html')
