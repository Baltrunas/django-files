# -*- coding: utf-8 -*
from django.contrib import admin
from django.conf import settings
from files.models import Category
from files.models import File


if 'hvad' in settings.INSTALLED_APPS and hasattr(settings, 'LANGUAGES'):
	from hvad.admin import TranslatableAdmin
	BaseAdminModel = TranslatableAdmin
else:
	BaseAdminModel = admin.ModelAdmin


class CategoryAdmin(BaseAdminModel):
	list_display = ['__unicode__', 'slug', 'special', 'public']
	search_fields = ['__unicode__', 'slug', 'special', 'public']
	list_editable = ['special', 'public']
	list_filter = ['special', 'public']

admin.site.register(Category, CategoryAdmin)


class FileAdmin(BaseAdminModel):
	list_display = ['__unicode__', 'category', 'file', 'downloads', 'public', 'created_at', 'updated_at']
	search_fields = ['__unicode__', 'category', 'file', 'downloads', 'public', 'created_at', 'updated_at']
	list_editable = ['public']
	list_filter = ['public', 'category']

admin.site.register(File, FileAdmin)
