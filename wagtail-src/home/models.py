from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import StreamField, RichTextField
from wagtail.models import Page
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.models import Image
from wagtailcodeblock.blocks import CodeBlock


# ========== CUSTOM BLOCKS ==========

class HeadingBlock(blocks.StructBlock):
    text = blocks.CharBlock(required=True, help_text="Text for the heading")
    size = blocks.ChoiceBlock(
        choices=[('h2', 'Heading 2'), ('h3', 'Heading 3'), ('h4', 'Heading 4')],
        default='h2',
        required=True,
        help_text="Size of the heading"
    )

    class Meta:
        template = 'blocks/heading_block.html'
        icon = 'title'
        label = 'Heading'


class CertificateBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    link = blocks.URLBlock(required=False)
    description = blocks.TextBlock(required=False)

    class Meta:
        template = 'blocks/certificate_block.html'
        icon = 'doc-full'
        label = 'Certificate'


# ========== HOMEPAGE ==========

class HomePage(Page):
    subtitle = models.CharField(max_length=255, blank=True, help_text="Subtitle for the homepage")
    intro_text = RichTextField(blank=True, help_text="Introductory text for the homepage")

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('intro_text'),
    ]


# ========== ABOUT ME PAGE ==========

class AboutMePage(Page):
    profile_image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    bio = RichTextField(blank=True)
    highlights = StreamField([
        ('certificate', CertificateBlock()),
        ('paragraph', blocks.RichTextBlock()),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('profile_image'),
        FieldPanel('bio'),
        FieldPanel('highlights'),
    ]


# ========== WRITEUP LISTING PAGE ==========

class WriteupPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    subpage_types = ['WriteupItemPage']


# ========== INDIVIDUAL WRITEUP ITEM PAGE ==========

class WriteupItemPage(Page):
    summary = models.CharField(max_length=300, blank=True)
    body = StreamField([
        ('heading', HeadingBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('code', CodeBlock(label='Code')),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('summary'),
        FieldPanel('body'),
    ]

    parent_page_types = ['WriteupPage']
