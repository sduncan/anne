from django.conf.urls import patterns, url

from page import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^photography/', views.photo, name='photo'),
    url(r'^art/', views.art, name='art'),
    url(r'^design/', views.design, name='design'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^anneadminlogin/', views.anneadminlogin, name='anneadminlogin'),
    url(r'^anneadmin/', views.anneadmin, name='anneadmin'),
)
