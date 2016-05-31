from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .models import File


def download(request, id):
	requested_file = get_object_or_404(File, id=id, public=True)
	requested_file.downloads += 1
	requested_file.save()

	return redirect(requested_file.file.url, permanent=True)
