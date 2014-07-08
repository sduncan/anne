from django.conf.urls import patterns, url

from photography import views

urlpatterns = patterns('',
    url(r'^photography/', views.photography, name='photography'),
)
