from django.conf.urls import patterns, url

from anneadmin import views

urlpatterns = patterns('',
    url(r'^login$', views.anneadmin_login, name='login'),
    url(r'^anneadmin$', views.anneadmin, name='main'),
)
