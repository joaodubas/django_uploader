# encoding: utf-8
from django.conf.urls import patterns, url
from .views import ImageCreateView, ImageUpdateView


urlpatterns = patterns('',
    url(r'^$', ImageCreateView.as_view(), name='image_create'),
    url(r'^(?P<pk>\d+)/$', ImageUpdateView.as_view(), name='image_update'),
)
