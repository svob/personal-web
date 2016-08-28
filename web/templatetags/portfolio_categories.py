from django import template
from django.template.loader import render_to_string

from web.models import PortfolioCategory

register = template.Library()


@register.simple_tag
def categories():
    categories = PortfolioCategory.objects.all()
    return render_to_string('web/portfolio-categories-box.html', {'categories':categories})