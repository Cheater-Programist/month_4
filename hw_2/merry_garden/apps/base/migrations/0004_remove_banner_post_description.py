# Generated by Django 5.0.3 on 2024-03-21 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_banner_image_1_banner_image_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='post_description',
        ),
    ]
