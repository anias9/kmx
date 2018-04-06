# Generated by Django 2.0.3 on 2018-04-05 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('komiksy', '0017_auto_20180404_0230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comic',
            name='tag',
        ),
        migrations.AlterField(
            model_name='elementy',
            name='text1',
            field=models.CharField(blank=True, default=' ', max_length=100, verbose_name='Tekst dla pierwszej postaci'),
        ),
        migrations.AlterField(
            model_name='elementy',
            name='text2',
            field=models.CharField(blank=True, default=' ', max_length=100, verbose_name='Tekst dla drugiej postaci'),
        ),
    ]
