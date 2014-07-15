from django.shortcuts import render
from django.views.generic import FormView
from django import forms

class AnneAdminForm(forms.Form):
    photo_submit = forms.ImageField()
    

class AnneAdminView(FormView):
    template_name = 'admin.html'
    form_class = AnneAdminForm

class AnneAdminLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.PasswordInput()

class AnneAdminLoginView(FormView):
    template_name = 'login.html'
    form_class = AnneAdminLoginForm

    def dispatch(self):

