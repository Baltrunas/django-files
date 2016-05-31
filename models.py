from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


from helpful.fields import upload_to


class File(models.Model):
	content_type = models.ForeignKey(ContentType, verbose_name=_('Content Type'))
	object_id = models.PositiveIntegerField(_('Object ID'))
	content_object = GenericForeignKey('content_type', 'object_id')

	name = models.CharField(_('Name'), max_length=255)
	description = models.TextField(_('Description'), blank=True)
	group = models.CharField(_('Group media'), max_length=64, blank=True)

	file = models.FileField(_('File'), upload_to=upload_to)

	created = models.DateTimeField(_('dateCreated'), blank=True, null=True)
	order = models.PositiveSmallIntegerField(_('Sort ordering'), default=500)

	downloads = models.PositiveIntegerField(_('Downloads'), editable=False, default=0)

	public = models.BooleanField(_('Public'), default=True)
	created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
	updated_at = models.DateTimeField(_('Updated at'), auto_now=True)


	def ext(self):
		filename = self.file.url.split('.')
		ext = filename[len(filename) - 1].lower()
		return ext

	def type(self):
		if self.ext() in ['jpg', 'png', 'gif']:
			return 'image'
		elif self.ext() in ['avi', 'mp4', 'oog', 'flw']:
			return 'video'
		else:
			return 'file'

	def dependent_from(self):
		return self.content_object

	@models.permalink
	def get_absolute_url(self):
		return ('files_download', (), {'id': self.id})

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['created_at']
		verbose_name = _('File')
		verbose_name_plural = _('Files')


# FileProperty
# 	key

# FilePropertyFalue
# 	key = FileProperty
# 	value = text


# latitude, longitude
# ObjectFilesMasthave
# 	FileProperty
