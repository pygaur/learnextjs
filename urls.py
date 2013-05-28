from django.conf.urls.defaults import patterns, include, url
import os
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

static = os.path.join(
    os.path.dirname(__file__) , 'static'
)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'extjs.views.home', name='home'),
    url(r'^', include('userapp.urls')),
    url(r'^static/(?P<path>.*)$' , 'django.views.static.serve' ,
        {'document_root' : static }),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
