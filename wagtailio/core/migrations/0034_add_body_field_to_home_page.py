# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-10 13:25
from __future__ import unicode_literals

from django.db import migrations

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailcore", "0030_index_on_pagerevision_created_at"),
        ("wagtailforms", "0003_capitalizeverbose"),
        ("wagtailredirects", "0005_capitalizeverbose"),
        ("core", "0033_auto_20160729_1200"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="homepagenew",
            name="listing_image",
        ),
        migrations.RemoveField(
            model_name="homepagenew",
            name="page_ptr",
        ),
        migrations.RemoveField(
            model_name="homepagenew",
            name="social_image",
        ),
        migrations.AddField(
            model_name="homepage",
            name="body",
            field=wagtail.fields.StreamField(
                (
                    (
                        "banner",
                        wagtail.blocks.StructBlock(
                            (
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(max_length=128),
                                ),
                                (
                                    "sub_title",
                                    wagtail.blocks.CharBlock(max_length=128),
                                ),
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "background",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    "links",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            (
                                                (
                                                    "link_text",
                                                    wagtail.blocks.CharBlock(),
                                                ),
                                                (
                                                    "link_text_bold",
                                                    wagtail.blocks.CharBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "link_page",
                                                    wagtail.blocks.PageChooserBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "link_url",
                                                    wagtail.blocks.CharBlock(
                                                        required=False
                                                    ),
                                                ),
                                            )
                                        )
                                    ),
                                ),
                            )
                        ),
                    ),
                    (
                        "brands",
                        wagtail.blocks.StructBlock(
                            (
                                ("title", wagtail.blocks.CharBlock(required=True)),
                                (
                                    "brands",
                                    wagtail.blocks.ListBlock(
                                        wagtail.images.blocks.ImageChooserBlock()
                                    ),
                                ),
                            )
                        ),
                    ),
                    (
                        "features",
                        wagtail.blocks.StructBlock(
                            (
                                ("title", wagtail.blocks.CharBlock()),
                                (
                                    "subtitle",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                                (
                                    "all_features_page",
                                    wagtail.blocks.PageChooserBlock(required=False),
                                ),
                                (
                                    "features",
                                    wagtail.blocks.ListBlock(
                                        wagtail.snippets.blocks.SnippetChooserBlock(
                                            "features.FeatureDescription"
                                        )
                                    ),
                                ),
                            )
                        ),
                    ),
                    (
                        "testimonials",
                        wagtail.blocks.ListBlock(
                            wagtail.blocks.StructBlock(
                                (
                                    ("quote", wagtail.blocks.TextBlock()),
                                    ("author", wagtail.blocks.CharBlock()),
                                    (
                                        "link",
                                        wagtail.blocks.URLBlock(required=False),
                                    ),
                                )
                            ),
                            icon="group",
                        ),
                    ),
                    (
                        "code",
                        wagtail.blocks.StructBlock(
                            (
                                ("title", wagtail.blocks.CharBlock()),
                                (
                                    "subtitle",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                                (
                                    "code",
                                    wagtail.blocks.StructBlock(
                                        (
                                            (
                                                "language",
                                                wagtail.blocks.ChoiceBlock(
                                                    choices=[
                                                        ("bash", "Bash/Shell"),
                                                        ("css", "CSS"),
                                                        (
                                                            "django",
                                                            "Django templating language",
                                                        ),
                                                        ("html", "HTML"),
                                                        ("javascript", "Javascript"),
                                                        ("python", "Python"),
                                                        ("scss", "SCSS"),
                                                    ]
                                                ),
                                            ),
                                            ("code", wagtail.blocks.TextBlock()),
                                        )
                                    ),
                                ),
                                (
                                    "link",
                                    wagtail.blocks.StructBlock(
                                        (
                                            (
                                                "link_text",
                                                wagtail.blocks.CharBlock(),
                                            ),
                                            (
                                                "link_text_bold",
                                                wagtail.blocks.CharBlock(
                                                    required=False
                                                ),
                                            ),
                                            (
                                                "link_page",
                                                wagtail.blocks.PageChooserBlock(
                                                    required=False
                                                ),
                                            ),
                                            (
                                                "link_url",
                                                wagtail.blocks.CharBlock(
                                                    required=False
                                                ),
                                            ),
                                        )
                                    ),
                                ),
                            )
                        ),
                    ),
                    (
                        "showcases",
                        wagtail.blocks.StructBlock(
                            (
                                ("title", wagtail.blocks.CharBlock()),
                                (
                                    "subtitle",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                                (
                                    "more_link",
                                    wagtail.blocks.StructBlock(
                                        (
                                            (
                                                "link_text",
                                                wagtail.blocks.CharBlock(),
                                            ),
                                            (
                                                "link_text_bold",
                                                wagtail.blocks.CharBlock(
                                                    required=False
                                                ),
                                            ),
                                            (
                                                "link_page",
                                                wagtail.blocks.PageChooserBlock(
                                                    required=False
                                                ),
                                            ),
                                            (
                                                "link_url",
                                                wagtail.blocks.CharBlock(
                                                    required=False
                                                ),
                                            ),
                                        ),
                                        required=False,
                                    ),
                                ),
                                (
                                    "items",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            (
                                                (
                                                    "title",
                                                    wagtail.blocks.CharBlock(),
                                                ),
                                                (
                                                    "subtitle",
                                                    wagtail.blocks.CharBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "link_url",
                                                    wagtail.blocks.URLBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(),
                                                ),
                                            )
                                        )
                                    ),
                                ),
                            )
                        ),
                    ),
                    (
                        "promo_texts",
                        wagtail.blocks.StructBlock(
                            (
                                ("title", wagtail.blocks.CharBlock()),
                                (
                                    "texts",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            (
                                                (
                                                    "title",
                                                    wagtail.blocks.CharBlock(),
                                                ),
                                                (
                                                    "text",
                                                    wagtail.blocks.RichTextBlock(),
                                                ),
                                            )
                                        )
                                    ),
                                ),
                            )
                        ),
                    ),
                ),
                default={},
            ),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="HomePageNew",
        ),
    ]
