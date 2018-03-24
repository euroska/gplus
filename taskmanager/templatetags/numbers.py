from django import template

register = template.Library()


@register.filter(name='int')
def toint(value):
    if value:
        return int(value)

    return None
