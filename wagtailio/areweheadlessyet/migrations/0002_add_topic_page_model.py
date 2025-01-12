# Generated by Django 3.2.8 on 2022-01-25 14:05

from django.db import migrations, models
import django.db.models.deletion

import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailcore", "0066_collection_management_permissions"),
        ("images", "0010_add_duplicatefindingmixin"),
        ("areweheadlessyet", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="areweheadlessyethomepage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "section",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                (
                                    "content",
                                    wagtail.blocks.StreamBlock(
                                        [
                                            (
                                                "text",
                                                wagtail.blocks.RichTextBlock(),
                                            ),
                                            (
                                                "link_group",
                                                wagtail.blocks.StreamBlock(
                                                    [
                                                        (
                                                            "link",
                                                            wagtail.blocks.StructBlock(
                                                                [
                                                                    (
                                                                        "link",
                                                                        wagtail.blocks.URLBlock(
                                                                            required=True
                                                                        ),
                                                                    ),
                                                                    (
                                                                        "link_text",
                                                                        wagtail.blocks.CharBlock(
                                                                            required=True
                                                                        ),
                                                                    ),
                                                                ]
                                                            ),
                                                        )
                                                    ]
                                                ),
                                            ),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "news",
                        wagtail.blocks.StreamBlock(
                            [
                                (
                                    "blog_post",
                                    wagtail.blocks.PageChooserBlock(
                                        page_type=["blog.BlogPage"]
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "topics",
                        wagtail.blocks.StructBlock(
                            [("title", wagtail.blocks.CharBlock())]
                        ),
                    ),
                ]
            ),
        ),
        migrations.CreateModel(
            name="AreWeHeadlessYetTopicPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "social_text",
                    models.CharField(
                        blank=True,
                        help_text="Description of this page as it should appear when shared on social networks, or in Google results",
                        max_length=255,
                        verbose_name="Meta description",
                    ),
                ),
                (
                    "listing_intro",
                    models.TextField(
                        blank=True,
                        help_text="Summary of this page to display when this is linked from elsewhere in the site.",
                    ),
                ),
                (
                    "status_color",
                    models.CharField(
                        choices=[
                            ("green", "green"),
                            ("amber", "amber"),
                            ("red", "red"),
                        ],
                        max_length=5,
                    ),
                ),
                ("introduction", models.TextField(blank=True)),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            ("text", wagtail.blocks.RichTextBlock()),
                            (
                                "section",
                                wagtail.blocks.StructBlock(
                                    [
                                        ("title", wagtail.blocks.CharBlock()),
                                        (
                                            "content",
                                            wagtail.blocks.StreamBlock(
                                                [
                                                    (
                                                        "text",
                                                        wagtail.blocks.RichTextBlock(),
                                                    ),
                                                    (
                                                        "link_group",
                                                        wagtail.blocks.StreamBlock(
                                                            [
                                                                (
                                                                    "link",
                                                                    wagtail.blocks.StructBlock(
                                                                        [
                                                                            (
                                                                                "link",
                                                                                wagtail.blocks.URLBlock(
                                                                                    required=True
                                                                                ),
                                                                            ),
                                                                            (
                                                                                "link_text",
                                                                                wagtail.blocks.CharBlock(
                                                                                    required=True
                                                                                ),
                                                                            ),
                                                                        ]
                                                                    ),
                                                                )
                                                            ]
                                                        ),
                                                    ),
                                                ]
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "news",
                                wagtail.blocks.StreamBlock(
                                    [
                                        (
                                            "blog_post",
                                            wagtail.blocks.PageChooserBlock(
                                                page_type=["blog.BlogPage"]
                                            ),
                                        )
                                    ]
                                ),
                            ),
                        ]
                    ),
                ),
                (
                    "listing_image",
                    models.ForeignKey(
                        blank=True,
                        help_text="Image to display along with summary, when this page is linked from elsewhere in the site.",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="images.wagtailioimage",
                    ),
                ),
                (
                    "social_image",
                    models.ForeignKey(
                        blank=True,
                        help_text="Image to appear alongside 'Meta description', particularly for sharing on social networks",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="images.wagtailioimage",
                        verbose_name="Meta image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page", models.Model),
        ),
    ]
