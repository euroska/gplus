from django import template

register = template.Library()


@register.filter(name='int')
def toint(value):
    '''
    Convert str to int (in template filter on issue list
    '''
    if value:
        return int(value)

    return None
