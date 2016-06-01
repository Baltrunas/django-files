from django.contrib import admin

from .models import File
from .models import FileKey
from .models import FileProperty


class FileAdmin(admin.ModelAdmin):
	list_display = ['name', 'file', 'downloads', 'public', 'created_at', 'updated_at']
	search_fields = ['name', 'file', 'downloads', 'public', 'created_at', 'updated_at']
	list_editable = ['public']
	list_filter = ['public', 'group']

admin.site.register(File, FileAdmin)
admin.site.register(FileKey)
admin.site.register(FileProperty)
