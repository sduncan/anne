from django.conf.urls import patterns, url

from design import views

urlpatterns = patterns('',
    url(r'^$', views.design, name='design'),
)
