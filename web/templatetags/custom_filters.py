
from django import template


register = template.Library()


@register.filter
def get_item(dict_object, key):
    if not isinstance(dict_object, dict):
        return ''
    return dict_object.get(key)
