from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail import blocks


class Pricing(Page):
    # Standard Plan
    standard_price = models.DecimalField(
        max_digits=6, decimal_places=2, default=30.00, help_text="Base cost per month (€)"
    )
    standard_device_cost = models.DecimalField(
        max_digits=6, decimal_places=2, default=2.00, help_text="Cost per device per month (€)"
    )

    standard_features = StreamField(
        [("feature", blocks.CharBlock(label="Feature"))],
        use_json_field=True,
        null=True,
        blank=True,
        default=None,
        help_text="List of Standard plan features",
    )

    # Premium Plan
    premium_price = models.DecimalField(
        max_digits=6, decimal_places=2, default=60.00, help_text="Base cost per month (€)"
    )
    premium_features = StreamField(
        [("feature", blocks.CharBlock(label="Feature"))],
        use_json_field=True,
        null=True,
        blank=True,
        default=None,
        help_text="List of Premium plan features",
    )

    content_panels = Page.content_panels + [
        FieldPanel("standard_price"),
        FieldPanel("standard_device_cost"),
        FieldPanel("standard_features"),
        FieldPanel("premium_price"),
        FieldPanel("premium_features"),
    ]
