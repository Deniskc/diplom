# Generated by Django 5.1.4 on 2025-03-12 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_news_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, max_length=256, null=True, unique=True, verbose_name='URL'),
        ),
    ]
