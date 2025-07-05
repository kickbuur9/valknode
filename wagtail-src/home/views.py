from django.shortcuts import render
from .models import Quote
import random

def page_not_found(request, exception):
    """
    Custom 404 view to display a single random quote.
    """
    quote = Quote.objects.order_by('?').first()  # Get 1 random quote

    context = {
        'quote': quote,
    }

    return render(request, '404.html', context, status=404)
