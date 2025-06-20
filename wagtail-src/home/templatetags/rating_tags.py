from django import template
from django.utils.safestring import mark_safe
import math

register = template.Library()

@register.filter
def render_rating(value):
    if value is None:
        return ""

    try:
        rating = float(value)
    except (ValueError, TypeError):
        return ""

    full_circles = int(math.floor(rating))
    half_circle = (rating - full_circles) >= 0.5
    empty_circles = 5 - full_circles - (1 if half_circle else 0)

    icons = []
    icons.extend(['<i class="fa-solid fa-circle"></i>'] * full_circles)

    if half_circle:
        icons.append('<i class="fa-solid fa-circle-half-stroke"></i>')

    icons.extend(['<i class="fa-regular fa-circle"></i>'] * empty_circles)

    return mark_safe(' '.join(icons))
