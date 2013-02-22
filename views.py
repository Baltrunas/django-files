# -*- coding: utf-8 -*
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
# from files.models import File
from files.models import Category


def files_category(request, slug):
	context = {}
	context['files_category'] = get_object_or_404(Category, slug=slug)
	return render_to_response('files/category.html', context, context_instance=RequestContext(request))
