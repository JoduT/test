# Generated by Django 4.2.3 on 2023-07-22 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements81', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisements81',
            name='bu',
            field=models.BooleanField(default=False, help_text='Был ли товар в бывшем использовании', verbose_name='б/у'),
        ),
    ]
