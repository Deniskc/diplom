# Generated by Django 5.1.4 on 2025-03-06 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_students_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер телефона'),
        ),
    ]
