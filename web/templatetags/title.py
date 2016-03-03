from django import template

from web.models import Me

register = template.Library()


@register.simple_tag
def title():
    me = Me.objects.all()[0]
    return me.name + ' ' + me.surname