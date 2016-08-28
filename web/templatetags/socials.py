from django import template
from django.template.loader import render_to_string

from web.models import Me

register = template.Library()


@register.simple_tag
def socials():
    socials = Me.get_solo().social_set.all()
    return render_to_string('web/socials-list.html', {'socials':socials})