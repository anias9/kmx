# Generated by Django 2.0.3 on 2018-04-04 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('komiksy', '0015_auto_20180404_0210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comic',
            old_name='element',
            new_name='elementy',
        ),
    ]
