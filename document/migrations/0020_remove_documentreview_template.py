# Generated by Django 3.1.7 on 2021-05-29 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0019_auto_20210530_0521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentreview',
            name='template',
        ),
    ]
