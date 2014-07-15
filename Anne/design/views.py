from django.shortcuts import render
from django import forms
from django.views.generic import FormView

from design.models import DesignModel

# Create your views here.


class DesignForm(forms.ModelForm):

    class Meta:
        model = DesignModel
        fields = ['picture_of_work', 'price', 'name']

class DesignView(FormView):

    form_class = DesignForm
    template_name = 'design.html'