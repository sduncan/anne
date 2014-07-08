from django.conf.urls import patterns, url

from anneadmin import views

urlpatterns = patterns('',
    url(r'^anneadmin/login', views.login, name='login'),
    url(r'^anneadmin/interface', views.interface, name='interface'),
)
