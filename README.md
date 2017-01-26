install
'apps.files',
url(r'^files/', include('apps.files.urls')),
python manage.py migrate

req	
	from helpful.fields import upload_to



downloads_list.html
downloads_icons.html

thumbnail.html
slider.html

thumbnail_outside.html
slider_outside.html


{% load files %}
{% files block_item 'awards' tpl='files/thumbnail.html' size='200x200' %}