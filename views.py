# -*- coding: utf-8 -*
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from files.models import File
from files.models import Category

from django.utils.translation import ugettext_lazy as _
from django import http


def files_categories(request):
	context = {}
	context['title'] = _('Files categories')
	context['categories'] = Category.objects.filter(public=True)
	return render_to_response('files/all.html', context, context_instance=RequestContext(request))


def files_category(request, slug):
	context = {}
	context['category'] = get_object_or_404(Category, slug=slug)
	context['title'] = context['category'].name
	context['category_list'] = Category.objects.filter(public=True)
	return render_to_response('files/category.html', context, context_instance=RequestContext(request))


def files_download(request, id):
	context = {}
	context['file'] = get_object_or_404(File, id=id)
	context['file'].download()
	return http.HttpResponsePermanentRedirect(context['file'].file.url)
