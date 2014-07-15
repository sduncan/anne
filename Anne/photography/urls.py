from django.conf.urls import patterns, url

from photography import views

urlpatterns = patterns('',
                       url(r'^$', views.PhotoView.as_view(), name='photography'),
                       )
