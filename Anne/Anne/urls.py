from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Anne.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('home.urls')),
    url(r'^art/', include('art.urls')),
    url(r'^photography/', include('photography.urls')),
    url(r'^design/', include('design.urls')),
    url(r'^anneadmin/', include('anneadmin.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^admin/', include(admin.site.urls)),
)