# Generated by Django 5.1.4 on 2025-03-20 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_remove_curses_hours_alter_curses_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curses',
            name='price',
            field=models.IntegerField(blank=True, default=169554, null=True, verbose_name='Цена, в руб.'),
        ),
    ]
