# Generated by Django 5.0.3 on 2024-03-11 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='user name')),
                ('lastname', models.CharField(max_length=255, verbose_name='user surname')),
                ('job', models.CharField(max_length=255, verbose_name='user job')),
                ('image', models.ImageField(upload_to='UserInfo', verbose_name='user image')),
                ('description', models.TextField(verbose_name='user description')),
                ('age', models.IntegerField(verbose_name='user age')),
                ('email', models.EmailField(max_length=254, verbose_name='user email')),
                ('adsress', models.CharField(max_length=255, verbose_name='user address')),
                ('youtube', models.URLField(verbose_name='YouTube')),
                ('instagram', models.URLField(verbose_name='Instagram')),
                ('whatsapp', models.URLField(verbose_name='Whatsapp')),
                ('telegram', models.URLField(verbose_name='Telegram')),
                ('facebook', models.URLField(verbose_name='Facebook')),
            ],
            options={
                'verbose_name': 'User admin',
                'verbose_name_plural': 'Users admin',
            },
        ),
    ]
