from django import template

register = template.Library()

def show_link(list, slug):
	for it in list:
		if it.slug==slug:
			return '<a href="%s">%s</a>' %  (it.get_absolute_url(), it.title_ru);
	return 'not found:', slug
	
def cut(list, slug):
	return "WOW!!!"	
	
register.filter(show_link)	
