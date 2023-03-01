from django import template
from django.http import Http404

from ..models import *

register = template.Library()

@register.inclusion_tag('menu_tags.html')
def get_menu(url, btn):
    model = ItemMenu.objects.select_related('menu', 'parent').filter(menu__url=url)

    if not model:
        raise Http404

    if btn is None:
        selected = 0
    else:
        selected = btn

    menu = {}

    for i in model:
        if i.parent:
            if i.parent in menu.keys():
                menu[i.parent].append(i)
            else:
                menu[i.parent] = [i]
        else:
            menu[i] = []

    return {'menu': menu, 'selected': selected}