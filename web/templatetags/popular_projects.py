from django import template
from django.template.loader import render_to_string

from web.models import Project

register = template.Library()


@register.simple_tag
def popular_projects():
    posts = Project.objects.order_by('-hit_count_generic__hits')[:4]
    return render_to_string('web/popular-projects.html', {'posts':posts})