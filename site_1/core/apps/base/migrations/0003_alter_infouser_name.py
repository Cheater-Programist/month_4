# Generated by Django 5.0.2 on 2024-03-07 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_infouser_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infouser',
            name='name',
            field=models.CharField(max_length=30, verbose_name='user name'),
        ),
    ]
