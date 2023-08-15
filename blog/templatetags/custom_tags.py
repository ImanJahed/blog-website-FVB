from django import template

register = template.Library()


@register.filter()
def add_comma(value, arg):
    return value[:arg]