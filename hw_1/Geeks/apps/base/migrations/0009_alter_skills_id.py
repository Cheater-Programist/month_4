# Generated by Django 5.0.3 on 2024-03-14 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
