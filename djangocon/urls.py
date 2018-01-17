﻿"""
Definition of urls for djangocon.
"""

from datetime import datetime
from django.conf.urls import url, include

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^anotherpage/', 'app.views.anotherpage', name='anotherpage'),
    # url(r'^additional_resources/', 'app.views.additional_resources', name='additional_resources'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
