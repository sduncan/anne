from django.shortcuts import render

# Create your views here.
from Anne import settings

def anneadmin_login(request):
    return render(request,'login.html')

def anneadmin(request):
    return render(request,'admin.html')
