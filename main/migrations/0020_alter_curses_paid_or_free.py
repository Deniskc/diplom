# Generated by Django 5.1.4 on 2025-03-13 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_remove_students_paid_or_free_curses_paid_or_free'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curses',
            name='paid_or_free',
            field=models.CharField(blank=True, default='б', max_length=2, null=True, verbose_name='Бюджет/Внебюджет (б/вб)'),
        ),
    ]
