from django.views.generic import TemplateView
# Create your views here.
from Anne import settings

class ContactView(TemplateView):
    template_name = "contact.html"
