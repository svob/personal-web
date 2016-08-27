from django import template

register = template.Library()

@register.filter
def spacedash(value):
    value.replace(" ", "-")