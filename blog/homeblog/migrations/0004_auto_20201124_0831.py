# Generated by Django 3.1.3 on 2020-11-24 07:31

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('homeblog', '0003_auto_20201124_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='keywords',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=tinymce.models.HTMLField(),
        ),
    ]
