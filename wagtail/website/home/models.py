from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField


class HomePage(Page):
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]


class GeneralPage(Page):
    body = RichTextField(blank=True)

    parent_page_types = ['home.HomePage']
    subpage_types = []

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
