# Generated by Django 5.0.3 on 2024-03-13 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_service'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Service', 'verbose_name_plural': 'Services'},
        ),
    ]
