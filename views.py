# -*- coding: utf-8 -*
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404

from django.template import RequestContext

from files.models import File
from files.models import Category

from django.utils.translation import ugettext_lazy as _
from django import http


def categories(request):
	context = {}
	context['categories'] = Category.objects.filter(public=True, special=False)
	context['title'] = _('Files')
	return render_to_response('files/categories.html', context, context_instance=RequestContext(request))


def category(request, slug):
	context = {}
	context['category'] = get_object_or_404(Category, slug=slug, public=True, special=False)
	context['title'] = context['category'].name
	return render_to_response('files/category.html', context, context_instance=RequestContext(request))


def download(request, id):
	context = {}
	context['file'] = get_object_or_404(File, id=id, public=True)
	context['file'].download()
	return http.HttpResponsePermanentRedirect(context['file'].file.url)
