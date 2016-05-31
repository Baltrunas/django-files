from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^download/(?P<id>[\d]+)/$', views.download, name='files_download'),
]
