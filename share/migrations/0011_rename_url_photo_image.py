# Generated by Django 4.0.3 on 2022-05-31 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0010_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='url',
            new_name='image',
        ),
    ]
