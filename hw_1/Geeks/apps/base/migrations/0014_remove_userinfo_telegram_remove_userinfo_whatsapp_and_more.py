# Generated by Django 5.0.3 on 2024-03-14 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='telegram',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='whatsapp',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='youtube',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='github',
            field=models.URLField(default=1, verbose_name='Github'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='linkedin',
            field=models.URLField(default=1, verbose_name='Linkedin'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='twitter',
            field=models.URLField(default=1, verbose_name='Twitter'),
            preserve_default=False,
        ),
    ]
