# -*- coding: utf-8 -*
from django.conf.urls import patterns
# from django.conf.urls import include
from django.conf.urls import url

urlpatterns = patterns('files.views',
	url(r'^(?P<slug>[-\D\w/_]+)/$', 'files_category', name='files_category'),
)
