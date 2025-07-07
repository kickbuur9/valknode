from django import template
from django.utils.text import slugify

register = template.Library()

@register.filter
def slugify_id(value):
    return slugify(value)
