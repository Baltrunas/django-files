django-files
============

# Install
* Add to INSTALLED_APPS ```'files',``` 
* Add to urls.py ```url(r'^files/', include('files.urls')),```
* ```manage.py syncdb```
* Add to head ```<link rel="stylesheet" href="/static/files/css/files.css">```


## Notise
If you want to use multilanguage you must instal [django-modeltranslation](https://github.com/deschler/django-modeltranslation), define LANGUAGES in settings and use 'middleware.SwitchLocaleMiddleware', to change languages.


# Todo
* Sub categories
* Template tags
	* For files
	* For category
* WYSIWYG editor integration


# Changelog
## 2014.03.01
* Change template
* Optimize views
* Update models

## 2014.02.28
* Downloads counter
* Change translation module

## 2013.02.21
* Start dev