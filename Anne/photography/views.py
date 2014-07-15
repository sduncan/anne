from django.shortcuts import render
from django import forms
from django.views.generic import FormView

from photography.models import PhotoModel

# Create your views here.


class PhotoForm(forms.ModelForm):

    class Meta:
        model = PhotoModel
        fields = ['picture_of_work', 'price', 'name']


class PhotoView(FormView):

    form_class = PhotoForm
    template_name = 'photo.html'

    def get_context_data(self, **kwargs):
        context = super(PhotoView, self).get_context_data(**kwargs)
        context['images'] = PhotoModel.objects.all()
        return context