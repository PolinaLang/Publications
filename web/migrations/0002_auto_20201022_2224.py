# Generated by Django 3.1.2 on 2020-10-22 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='datetime',
            new_name='date',
        ),
    ]
