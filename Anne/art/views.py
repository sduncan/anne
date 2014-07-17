from django.shortcuts import render
from django import forms
from django.views.generic import FormView

from art.models import ArtModel

# Create your views here.


class ArtForm(forms.ModelForm):

    class Meta:
        model = ArtModel
        fields = ['picture_of_work', 'price', 'name']


class ArtView(FormView):

    form_class = ArtForm
    template_name = 'art.html'

    def get_context_data(self, **kwargs):
        context = super(ArtView, self).get_context_data(**kwargs)
        context['images'] = ArtModel.objects.all()
        return context