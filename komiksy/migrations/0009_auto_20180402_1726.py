# Generated by Django 2.0.3 on 2018-04-02 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('komiksy', '0008_auto_20180314_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.ImageField(blank=True, null=True, upload_to='media')),
                ('character1', models.ImageField(blank=True, null=True, upload_to='media')),
                ('character2', models.ImageField(blank=True, null=True, upload_to='media')),
                ('chat1', models.ImageField(blank=True, null=True, upload_to='media')),
                ('chat2', models.ImageField(blank=True, null=True, upload_to='media')),
            ],
        ),
        migrations.RemoveField(
            model_name='comic',
            name='type',
        ),
        migrations.AlterField(
            model_name='comic',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Tytul'),
        ),
        migrations.AddField(
            model_name='elements',
            name='comics',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='komiksy.Comic'),
        ),
    ]
