# Generated by Django 5.0.2 on 2024-03-11 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_infouser_description_infouser_email_infouser_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Numbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.IntegerField(verbose_name='experience')),
                ('project', models.IntegerField(verbose_name='projects')),
                ('clientes', models.IntegerField(verbose_name='customers')),
            ],
        ),
    ]