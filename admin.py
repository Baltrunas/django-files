from django.contrib import admin

# from files.models import Category
from files.models import File


# class CategoryAdmin(admin.ModelAdmin):
# 	list_display = ['name', 'slug', 'special', 'public']
# 	search_fields = ['name', 'slug', 'special', 'public']
# 	list_editable = ['special', 'public']
# 	list_filter = ['special', 'public']

# admin.site.register(Category, CategoryAdmin)


# class FileAdmin(admin.ModelAdmin):
# 	list_display = ['name', 'category', 'file', 'downloads', 'public', 'created_at', 'updated_at']
# 	search_fields = ['name', 'category', 'file', 'downloads', 'public', 'created_at', 'updated_at']
# 	list_editable = ['public']
# 	list_filter = ['public', 'category']

# admin.site.register(File, FileAdmin)
