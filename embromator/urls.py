# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    # TODO
    # Embromator
    (r'^generate/sentences/(\d+)/$', 'generator.views.sentences'),
    # (r'^embromator/generate/paragraphs/\d+', ),  # TODO: Set method call

    #Admin
    url(r'^admin/', include(admin.site.urls)),
)
