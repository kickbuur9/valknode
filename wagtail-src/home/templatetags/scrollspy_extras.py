from django import template
from django.utils.text import slugify

register = template.Library()

@register.filter
def slugify_id(value):
    return slugify(value)

@register.filter
def get_range(value, start_value=0):
    return range(start_value, value)