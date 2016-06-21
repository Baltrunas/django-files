from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from .models import File, FileKey, FileProperty


class FilePropertyInline(admin.TabularInline):
	model = FileProperty
	extra = 0

class FileAdmin(admin.ModelAdmin):
	list_display = ['name', 'file', 'downloads', 'public', 'created_at', 'updated_at']
	search_fields = ['name', 'file', 'downloads', 'public', 'created_at', 'updated_at']
	list_editable = ['public']
	list_filter = ['public', 'group']
	inlines = [FilePropertyInline]

admin.site.register(File, FileAdmin)

admin.site.register(FileKey)
admin.site.register(FileProperty)


class FileInline(GenericStackedInline):
	model = File
	extra = 0
