# -*- coding: utf-8 -*
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns('files.views',
	url(r'^$', 'files_categories', name='files_categories'),
	url(r'^download/(?P<id>[\d]+)/$', 'files_download', name='files_download'),
	url(r'^(?P<slug>[-\D\w/_]+)/$', 'files_category', name='files_category'),
)
