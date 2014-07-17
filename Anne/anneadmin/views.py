from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from art.models import ArtModel
from design.models import DesignModel
from photography.models import PhotoModel
from anneadmin.models import UserModel

class AnneAdminForm(forms.Form):
    image_submit = forms.ImageField(required=True)
    upload_choice = forms.ChoiceField(required=True, choices=(("", "Select Category"), ("art", "Art"), ("photography", "Photo"), ("design", "Design")))
    piece_name = forms.CharField(required=True, max_length=100)
    price = forms.DecimalField(required=True, max_digits=7, decimal_places=2)

class AnneAdminView(FormView):
    template_name = 'admin.html'
    form_class = AnneAdminForm

    def form_valid(self, form):
        upload_type = form.cleaned_data['upload_choice']
        piece_name = form.cleaned_data['piece_name']
        piece_price = form.cleaned_data['price']
        image_of_piece = form.cleaned_data['image_submit']
        if upload_type == "art":
            art_piece = ArtModel(name=piece_name, price=piece_price, picture_of_work=image_of_piece)
            art_piece.save()
        if upload_type == "design":
            design_piece = DesignModel(name=piece_name, price=piece_price, picture_of_work=image_of_piece)
            design_piece.save()
        if upload_type == "photography":
            photo_piece = PhotoModel(name=piece_name, price=piece_price, picture_of_work=image_of_piece)
            photo_piece.save()
        return HttpResponseRedirect(reverse("main"))

# class AnneAdminLoginForm(forms.Form):
#     username = forms.CharField(required=True, max_length=20)
#     password = forms.PasswordInput()

class AnneAdminLoginView(TemplateView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.method == "POST":
            return HttpResponseRedirect(reverse("login"))
        else:
            try:
                user = UserModel.objects.get(username=request.GET['username'])
            except UserModel.DoesNotExist:
                return HttpResponseRedirect(reverse("login"))
            if user.password == request.GET['password']:
                return HttpResponseRedirect(reverse("main"))