# Generated by Django 5.0.2 on 2024-03-11 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_numbers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.AlterModelOptions(
            name='numbers',
            options={'verbose_name': 'Number', 'verbose_name_plural': 'Numbers'},
        ),
    ]
