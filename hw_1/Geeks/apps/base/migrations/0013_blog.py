# Generated by Django 5.0.3 on 2024-03-14 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Portfolio', verbose_name='Image')),
                ('data', models.DateField(verbose_name='Date')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
    ]
