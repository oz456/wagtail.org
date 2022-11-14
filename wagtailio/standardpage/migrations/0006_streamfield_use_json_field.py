# Generated by Django 3.2.16 on 2022-10-04 12:34

from django.db import migrations

import wagtail.blocks
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks

import wagtailio.utils.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("standardpage", "0005_update_templates"),
    ]

    operations = [
        migrations.AlterField(
            model_name="standardpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "h2",
                        wagtail.blocks.CharBlock(
                            form_classname="title",
                            icon="title",
                            template="patterns/components/streamfields/headings/heading-2.html",
                        ),
                    ),
                    (
                        "h3",
                        wagtail.blocks.CharBlock(
                            form_classname="title",
                            icon="title",
                            template="patterns/components/streamfields/headings/heading-3.html",
                        ),
                    ),
                    (
                        "h4",
                        wagtail.blocks.CharBlock(
                            form_classname="title",
                            icon="title",
                            template="patterns/components/streamfields/headings/heading-4.html",
                        ),
                    ),
                    (
                        "intro",
                        wagtail.blocks.RichTextBlock(
                            icon="pilcrow",
                            template="patterns/components/streamfields/rich_text_block/rich_text_block.html",
                        ),
                    ),
                    (
                        "paragraph",
                        wagtail.blocks.RichTextBlock(
                            icon="pilcrow",
                            template="patterns/components/streamfields/rich_text_block/rich_text_block.html",
                        ),
                    ),
                    (
                        "blockquote",
                        wagtail.blocks.CharBlock(
                            form_classname="title",
                            icon="openquote",
                            template="patterns/components/streamfields/quotes/standalone_quote_block.html",
                        ),
                    ),
                    (
                        "image",
                        wagtail.images.blocks.ImageChooserBlock(
                            icon="image",
                            template="patterns/components/streamfields/image/image.html",
                        ),
                    ),
                    (
                        "document",
                        wagtail.documents.blocks.DocumentChooserBlock(
                            icon="doc-full-inverse",
                            template="patterns/components/streamfields/document/document.html",
                        ),
                    ),
                    (
                        "imagecaption",
                        wagtail.blocks.StructBlock(
                            [
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                ("caption", wagtail.blocks.RichTextBlock()),
                            ],
                            label="Image caption",
                        ),
                    ),
                    (
                        "textimage",
                        wagtail.blocks.StructBlock(
                            [
                                ("text", wagtail.blocks.RichTextBlock()),
                                ("image", wagtail.images.blocks.ImageChooserBlock()),
                                (
                                    "background",
                                    wagtailio.utils.blocks.BackgroundColourChoiceBlock(),
                                ),
                                (
                                    "alignment",
                                    wagtailio.utils.blocks.SimpleImageFormatChoiceBlock(),
                                ),
                            ],
                            icon="image",
                        ),
                    ),
                    (
                        "colourtext",
                        wagtail.blocks.StructBlock(
                            [
                                ("text", wagtail.blocks.RichTextBlock()),
                                (
                                    "background",
                                    wagtailio.utils.blocks.BackgroundColourChoiceBlock(),
                                ),
                            ],
                            icon="pilcrow",
                        ),
                    ),
                    (
                        "calltoaction",
                        wagtail.blocks.StructBlock(
                            [
                                ("text", wagtail.blocks.RichTextBlock()),
                                (
                                    "background",
                                    wagtailio.utils.blocks.BackgroundColourChoiceBlock(),
                                ),
                            ],
                            icon="pilcrow",
                        ),
                    ),
                    (
                        "tripleimage",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "first_image",
                                    wagtail.images.blocks.ImageChooserBlock(),
                                ),
                                (
                                    "second_image",
                                    wagtail.images.blocks.ImageChooserBlock(),
                                ),
                                (
                                    "third_image",
                                    wagtail.images.blocks.ImageChooserBlock(),
                                ),
                            ],
                            icon="image",
                        ),
                    ),
                    (
                        "stats",
                        wagtail.blocks.ListBlock(
                            wagtail.blocks.StructBlock(
                                [
                                    (
                                        "image",
                                        wagtail.images.blocks.ImageChooserBlock(),
                                    ),
                                    ("stat", wagtail.blocks.CharBlock()),
                                    ("text", wagtail.blocks.CharBlock()),
                                ],
                                icon="code",
                            )
                        ),
                    ),
                    (
                        "embed",
                        wagtail.embeds.blocks.EmbedBlock(
                            icon="code",
                            template="patterns/components/streamfields/embed/embed.html",
                        ),
                    ),
                    (
                        "markdown",
                        wagtailio.utils.blocks.MarkDownBlock(
                            template="patterns/components/streamfields/code_block/code_block.html"
                        ),
                    ),
                    (
                        "codeblock",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "language",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("bash", "Bash/Shell"),
                                            ("css", "CSS"),
                                            ("django", "Django templating language"),
                                            ("html", "HTML"),
                                            ("javascript", "Javascript"),
                                            ("python", "Python"),
                                            ("scss", "SCSS"),
                                        ]
                                    ),
                                ),
                                ("code", wagtail.blocks.TextBlock()),
                            ],
                            template="patterns/components/streamfields/code_block/code_block.html",
                        ),
                    ),
                    (
                        "backers",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "gold_backers",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                ("name", wagtail.blocks.CharBlock()),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "url",
                                                    wagtail.blocks.URLBlock(
                                                        required=False
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                                (
                                    "silver_backers",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                ("name", wagtail.blocks.CharBlock()),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "url",
                                                    wagtail.blocks.URLBlock(
                                                        required=False
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                                (
                                    "bronze_backers",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                ("name", wagtail.blocks.CharBlock()),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "url",
                                                    wagtail.blocks.URLBlock(
                                                        required=False
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                                (
                                    "linked_backers",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                ("name", wagtail.blocks.CharBlock()),
                                                (
                                                    "url",
                                                    wagtail.blocks.URLBlock(
                                                        required=False
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                                (
                                    "named_backers",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [("name", wagtail.blocks.CharBlock())]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                ],
                use_json_field=True,
            ),
        ),
    ]
