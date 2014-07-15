from django.conf.urls import patterns, url

from anneadmin import views

urlpatterns = patterns('',
    url(r'^login$', views.AnneAdminLoginView.as_view(), name='login'),
    url(r'^anneadmin$', views.AnneAdminView.as_view(), name='main'),
)
