# encoding: utf-8
from django.conf.urls import patterns, url
from .views import ImageCreateView, ImageUpdateView, ImageDeleteView


urlpatterns = patterns('',
    url(r'^$', ImageCreateView.as_view(), name='image_create'),
    url(r'^(?P<pk>\d+)/$', ImageUpdateView.as_view(), name='image_update'),
    url(r'^delete/(?P<pk>\d+)/$', ImageDeleteView.as_view(), name='image_delete'),
)
