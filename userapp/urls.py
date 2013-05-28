from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from userapp.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', Index.as_view(), name='index'),
    url(r'signup/', Signup.as_view(), name='signup'),
    #url(r'signup/', 'userapp.views.signup', name='signup'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
