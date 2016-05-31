from django.contrib import admin

from .models import File


class FileAdmin(admin.ModelAdmin):
	list_display = ['name', 'file', 'downloads', 'public', 'created_at', 'updated_at']
	search_fields = ['name', 'file', 'downloads', 'public', 'created_at', 'updated_at']
	list_editable = ['public']
	list_filter = ['public', 'group']

admin.site.register(File, FileAdmin)
