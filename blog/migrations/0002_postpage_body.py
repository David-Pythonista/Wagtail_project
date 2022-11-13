# Generated by Django 4.1.3 on 2022-11-08 20:07

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postpage',
            name='body',
            field=wagtail.fields.StreamField([('h1', wagtail.blocks.CharBlock()), ('h2', wagtail.blocks.CharBlock()), ('paragraph', wagtail.blocks.RichTextBlock()), ('image_text', wagtail.blocks.StructBlock([('reverse', wagtail.blocks.BooleanBlock(required=False)), ('text', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('image_carousel', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('thumbnail_gallery', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))], blank=True, use_json_field=None),
        ),
    ]
