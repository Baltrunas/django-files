# -*- coding: utf-8 -*
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=255)
	description = models.TextField(verbose_name=_('Description'), blank=True)

	slug = models.SlugField(verbose_name=_('Slug'), unique=True)

	special = models.BooleanField(verbose_name=_('Special'), default=True)
	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def get_files(self):
		return self.files.filter(public=True)

	@models.permalink
	def get_absolute_url(self):
		return ('files_category', (), {'slug': self.slug})

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['created_at']
		verbose_name = _('Files Category')
		verbose_name_plural = _('Files Categories')


class File(models.Model):
	name = models.CharField(verbose_name=_('Name'), max_length=255)
	description = models.TextField(verbose_name=_('Description'), blank=True)

	category = models.ForeignKey(Category, related_name='files', verbose_name=_('Category'))

	file = models.FileField(verbose_name=_('File'), upload_to='files', blank=True)
	downloads = models.PositiveIntegerField(verbose_name=_('Downloads'), editable=False, default=0)

	public = models.BooleanField(verbose_name=_('Public'), default=True)
	created_at = models.DateTimeField(verbose_name=_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(verbose_name=_('Updated At'), auto_now=True)

	def download(self):
		self.downloads += 1
		self.save()

	def filetype(self):
		filename = self.file.url.split('.')
		filetype = filename[len(filename) - 1].lower()
		return filetype

	@models.permalink
	def get_absolute_url(self):
		return ('files_download', (), {'id': self.id})

	def __unicode__(self):
		return self.name

	class Meta:
		ordering = ['created_at']
		verbose_name = _('File')
		verbose_name_plural = _('Files')
