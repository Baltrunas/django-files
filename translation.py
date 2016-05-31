from modeltranslation.translator import translator
from modeltranslation.translator import TranslationOptions

from .models import File


class FileTranslationOptions(TranslationOptions):
	fields = ['name', 'description']

translator.register(File, FileTranslationOptions)
