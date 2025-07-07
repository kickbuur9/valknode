from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField, RichTextField
from wagtail.models import Page
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.models import Image
from wagtailcodeblock.blocks import CodeBlock

from wagtail.snippets.models import register_snippet

@register_snippet
class Quote(models.Model):
    text = models.TextField(
        verbose_name="Quote Text",
        help_text="The actual quote."
    )
    author = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Author",
        help_text="The author of the quote (optional)."
    )

    panels = [
        FieldPanel('text'),
        FieldPanel('author'),
    ]

    def __str__(self):
        return f'"{self.text}" - {self.author if self.author else "Unknown"}'

    class Meta:
        verbose_name = "Quote"
        verbose_name_plural = "Quotes"

class HeadingBlock(blocks.StructBlock):
    text = blocks.CharBlock(required=True, help_text="Text for the heading")
    size = blocks.ChoiceBlock(
        choices=[
            ('h2', 'Heading 2'),
            ('h3', 'Heading 3'),
            ('h4', 'Heading 4'),
        ],
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
    description = blocks.TextBlock(required=True)
    link = blocks.URLBlock(required=False)

    class Meta:
        icon = "doc-full"
        label = "Certificate"

class AboutMePage(Page):
    intro = RichTextField(blank=True)
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
        FieldPanel('intro'),
        FieldPanel('profile_image'),
        FieldPanel('bio'),
        FieldPanel('highlights'),
    ]

class HomePage(Page):
    def get_context(self, request):
        context = super().get_context(request)
        latest_posts = (
            Page.objects.live()
            .descendant_of(self)
            .exclude(id=self.id)
            .order_by('-first_published_at')[:3]
        )
        context['latest_posts'] = [p.specific for p in latest_posts]
        return context

class WriteupPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

    subpage_types = ['WriteupItemPage']


class WriteupItemPage(Page):
    summary = models.CharField(max_length=300, blank=True)
    author = models.CharField(
        max_length=100,
        blank=True,
        help_text="Name of the person who wrote this writeup"
    )
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        choices=[(x / 2, f"{x / 2}") for x in range(2, 11)],  # 1.0 to 5.0 in 0.5 steps
        blank=True,
        null=True,
        help_text="Optional rating between 1.0 and 5.0 (halves allowed)"
    )

    body = StreamField([
        ('heading', HeadingBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('code', CodeBlock(label='Code')),
    ], use_json_field=True, blank=True)

    background_image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    youtube_url = models.URLField(
        blank=True,
        null=True,
        help_text="Optional link to a YouTube video"
    )

    content_panels = Page.content_panels + [
        FieldPanel('summary'),
        FieldPanel('author'),
        FieldPanel('rating'),
        FieldPanel('background_image'),
        FieldPanel('body'),
        FieldPanel('youtube_url'),
    ]

    parent_page_types = ['WriteupPage']

    class Meta:
        verbose_name = "Writeup Item"

    @property
    def published_date(self):
        return self.first_published_at

    @property
    def updated_date(self):
        return self.last_published_at
