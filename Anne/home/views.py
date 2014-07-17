from django.views.generic import TemplateView
# Create your views here.
from Anne import settings

class HomeView(TemplateView):
    template_name = "home.html"
