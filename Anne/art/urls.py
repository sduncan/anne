from django.conf.urls import patterns, url

from art import views

urlpatterns = patterns('',
    url(r'^/art', views.art, name='art'),
)
