from django import template
register = template.Library()

from ..models import File


@register.simple_tag(takes_context=True)
def files(context, obj, group, tpl='files/media.html', size=''):
	page = context['page']
	context['size'] = size
	context['media_group'] = File.objects.filter(obj=obj, group=group, public=True)

	tpl = template.loader.get_template(tpl)
	return tpl.render(template.Context(context))
