from django.shortcuts import render

# Create your views here.
from Anne import settings

def home(request):
    return render(request,settings.BASE_DIR+'/page/templates/home.html')
