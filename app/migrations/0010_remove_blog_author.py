# Generated by Django 5.0 on 2025-02-01 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
    ]
