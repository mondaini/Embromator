# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

post_detail = DetailView.as_view(model=Post)
post_list = ListView.as_view(model=Post)

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    # TODO
    #Authentication
    #(r'^auth', ), #TODO: Set method call

    # TODO
    # Embromator
    (r'^embromator/generate/sentences/(\d+)/$', 'generator.views.sentences'), #TODO: Set method call
    # (r'^embromator/generate/paragraphs/\d+', ),#TODO: Set method call 

    #Admin
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #Blog Urls
    url(r'^post/(?P<pk>[a-z\d]+)/$', post_detail, name='post_detail'),
    url(r'^blog$', post_list, name='post_list'),
    url(r'^$', post_list, name='post_list'),
)
