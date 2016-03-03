from django import template
from django.template.loader import render_to_string

from web.models import Category

register = template.Library()


@register.simple_tag
def categories():
    categories = Category.objects.all()
    return render_to_string('web/categories-box.html', {'categories':categories})