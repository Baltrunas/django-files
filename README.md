django-files
============
# Install
* Add to INSTALLED_APPS 'files', 
* Add to urls.py url(r'^files/', include('files.urls')),
* manage.py syncdb
## Notise
If you want to use multilanguage you must instal hvad, define LANGUAGES in settings and use 'middleware.SwitchLocaleMiddleware', to change languages.

# Futures

# ToDo
* Sub categories?
* Template tags
* Downloads counter

# Changelog
## 2013.02.21
Start dev