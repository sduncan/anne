from django.conf.urls import patterns, url

from art import views

urlpatterns = patterns('',
                       url(r'^$', views.ArtView.as_view(), name='art'),
                       )
