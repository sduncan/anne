from django.conf.urls import patterns, url

from design import views

urlpatterns = patterns('',
    url(r'^design/', views.design, name='design'),
)
