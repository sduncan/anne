from django.conf.urls import patterns, url

from photography import views

urlpatterns = patterns('',
    url(r'^$', views.photography, name='photography'),
)
